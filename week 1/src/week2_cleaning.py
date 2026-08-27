import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_csv(filename: str) -> pd.DataFrame:
    """Load one CSV from the project data directory."""
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"{path} was not found. Download the Olist dataset first."
        )
    return pd.read_csv(path)


def profile_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Return a simple missing-value and data-type profile."""
    missing = df.isna().sum()
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing_count": missing,
        "missing_percent": (missing / len(df) * 100).round(2),
        "unique_count": df.nunique(dropna=True),
    }).sort_values("missing_percent", ascending=False)


def parse_order_dates(orders: pd.DataFrame) -> pd.DataFrame:
    """Convert Olist order timestamp columns to datetime."""
    df = orders.copy()

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    return df


def clean_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Clean orders and create delivery-related features."""
    df = parse_order_dates(orders)
    df = df.drop_duplicates().copy()

    df["delivery_days"] = (
        df["order_delivered_customer_date"]
        - df["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    df["late_flag"] = (
        df["order_delivered_customer_date"]
        > df["order_estimated_delivery_date"]
    ).astype("Int64")

    return df


def clean_products(products: pd.DataFrame) -> pd.DataFrame:
    """Standardize product categories and impute a basic numeric field."""
    df = products.copy()

    if "product_category_name" in df.columns:
        df["product_category_name"] = (
            df["product_category_name"]
            .astype("string")
            .str.strip()
            .str.lower()
            .fillna("unknown")
        )

    if "product_weight_g" in df.columns:
        df["product_weight_g"] = pd.to_numeric(
            df["product_weight_g"], errors="coerce"
        )
        df["product_weight_g"] = df["product_weight_g"].fillna(
            df["product_weight_g"].median()
        )

    return df


def iqr_bounds(series: pd.Series):
    """Return IQR-based lower and upper screening bounds."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


def aggregate_order_items(items: pd.DataFrame) -> pd.DataFrame:
    """Aggregate item-level values to the order level."""
    return (
        items.groupby("order_id")
        .agg(
            order_value=("price", "sum"),
            freight_value=("freight_value", "sum"),
            item_count=("order_item_id", "count"),
        )
        .reset_index()
    )


def build_clean_analysis_dataset(orders: pd.DataFrame, items: pd.DataFrame):
    """Build a clean order-level starter dataset."""
    orders_clean = clean_orders(orders)
    item_summary = aggregate_order_items(items)

    return orders_clean.merge(
        item_summary,
        on="order_id",
        how="left"
    )
