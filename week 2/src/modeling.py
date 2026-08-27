import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def train_delivery_regression(df: pd.DataFrame):
    """Train a simple baseline model for delivery duration."""
    features = ["order_value", "freight_value", "item_count"]
    target = "delivery_days"

    model_df = df.dropna(subset=[target]).copy()

    X = model_df[features]
    y = model_df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("regressor", LinearRegression()),
    ])

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5

    return model, {
        "MAE": round(mae, 3),
        "RMSE": round(rmse, 3),
    }


def cluster_sellers(seller_features: pd.DataFrame, n_clusters: int = 4):
    """Create seller segments using basic logistics features."""
    features = ["orders", "avg_freight", "avg_item_price"]

    X = seller_features[features].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10,
    )

    result = seller_features.copy()
    result["cluster"] = model.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, result["cluster"])

    return result, round(score, 3)
