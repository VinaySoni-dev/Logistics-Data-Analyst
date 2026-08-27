import pandas as pd


ORDER_DATE_COLUMNS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


def clean_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Clean order data and create delivery-related features."""
    df = orders.copy()

    for column in ORDER_DATE_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    # Delivery duration in days
    if {
        "order_purchase_timestamp",
        "order_delivered_customer_date",
    }.issubset(df.columns):
        df["delivery_days"] = (
            df["order_delivered_customer_date"]
            - df["order_purchase_timestamp"]
        ).dt.total_seconds() / 86400

    # Late delivery flag
    if {
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    }.issubset(df.columns):
        df["late_flag"] = (
            df["order_delivered_customer_date"]
            > df["order_estimated_delivery_date"]
        ).astype("Int64")

    return df


def aggregate_order_items(items: pd.DataFrame) -> pd.DataFrame:
    """Aggregate item-level price and freight information to order level."""
    return (
        items.groupby("order_id")
        .agg(
            order_value=("price", "sum"),
            freight_value=("freight_value", "sum"),
            item_count=("order_item_id", "count"),
        )
        .reset_index()
    )


def build_analysis_dataset(orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    """Create a basic order-level analytical dataset."""
    clean = clean_orders(orders)
    item_summary = aggregate_order_items(items)

    df = clean.merge(item_summary, on="order_id", how="left")

    return df
