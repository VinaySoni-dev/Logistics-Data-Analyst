from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV file from the project's data directory."""
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {path}. "
            "Download the Olist dataset and place the CSV in data/."
        )

    return pd.read_csv(path)


def load_core_data():
    """Load the main Olist tables required for Week 1 analysis."""
    orders = load_csv("olist_orders_dataset.csv")
    items = load_csv("olist_order_items_dataset.csv")
    customers = load_csv("olist_customers_dataset.csv")
    sellers = load_csv("olist_sellers_dataset.csv")
    products = load_csv("olist_products_dataset.csv")
    reviews = load_csv("olist_order_reviews_dataset.csv")

    return {
        "orders": orders,
        "items": items,
        "customers": customers,
        "sellers": sellers,
        "products": products,
        "reviews": reviews,
    }
