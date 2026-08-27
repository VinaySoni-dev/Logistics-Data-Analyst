import pandas as pd


def eligible_deliveries(df: pd.DataFrame) -> pd.DataFrame:
    """Return delivered orders with the fields required for KPI analysis."""
    required = ["delivery_days", "late_flag"]
    result = df.dropna(subset=required).copy()

    return result


def calculate_kpis(df: pd.DataFrame) -> dict:
    """Calculate the main Week 1 logistics KPIs."""
    data = eligible_deliveries(df)

    if data.empty:
        return {
            "on_time_delivery_rate": None,
            "average_delivery_days": None,
            "late_delivery_rate": None,
            "average_freight_per_order": None,
        }

    on_time_rate = (1 - data["late_flag"].mean()) * 100
    late_rate = data["late_flag"].mean() * 100

    return {
        "on_time_delivery_rate": round(on_time_rate, 2),
        "average_delivery_days": round(data["delivery_days"].mean(), 2),
        "late_delivery_rate": round(late_rate, 2),
        "average_freight_per_order": round(data["freight_value"].mean(), 2),
    }
