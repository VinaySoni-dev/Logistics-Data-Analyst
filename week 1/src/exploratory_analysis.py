import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_delivery_distribution(df: pd.DataFrame):
    """Plot the distribution of delivery time."""
    data = df.dropna(subset=["delivery_days"])

    sns.histplot(data["delivery_days"], bins=40, kde=True)
    plt.xlabel("Delivery Time (days)")
    plt.ylabel("Number of Orders")
    plt.title("Distribution of Delivery Time")
    plt.tight_layout()
    plt.show()


def monthly_late_rate(df: pd.DataFrame) -> pd.Series:
    """Calculate late delivery rate by purchase month."""
    data = df.dropna(subset=["late_flag"]).copy()

    data["month"] = (
        pd.to_datetime(data["order_purchase_timestamp"])
        .dt.to_period("M")
        .astype(str)
    )

    return data.groupby("month")["late_flag"].mean() * 100


def plot_monthly_late_rate(df: pd.DataFrame):
    rates = monthly_late_rate(df)

    rates.plot(kind="line", marker="o")
    plt.xlabel("Month")
    plt.ylabel("Late Delivery Rate (%)")
    plt.title("Monthly Late Delivery Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
