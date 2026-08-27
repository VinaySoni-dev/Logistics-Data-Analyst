import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def minmax_scale(df: pd.DataFrame, columns):
    """Scale selected columns to the range [0, 1]."""
    result = df.copy()
    scaler = MinMaxScaler()
    result[columns] = scaler.fit_transform(result[columns])
    return result, scaler


def standardize(df: pd.DataFrame, columns):
    """Standardize selected numeric columns using z-score scaling."""
    result = df.copy()
    scaler = StandardScaler()
    result[columns] = scaler.fit_transform(result[columns])
    return result, scaler


def validate_non_negative(df: pd.DataFrame, columns):
    """Return counts of negative values for variables expected to be non-negative."""
    return {
        column: int((df[column] < 0).sum())
        for column in columns
        if column in df.columns
    }
