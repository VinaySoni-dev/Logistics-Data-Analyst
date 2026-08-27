"""
Week 4: Logistics Predictive Modeling Script
Dataset: week4_logistics_predictive_model_dataset.csv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def main():
    # 1. Load Dataset
    df = pd.read_csv('week4_logistics_predictive_model_dataset.csv')
    
    # 2. Data Preprocessing
    df['Priority_Numeric'] = df['Priority'].map({'Standard': 0, 'Express': 1})
    
    features = [
        'Distance_km', 'Shipment_Weight_kg', 'Traffic_Level', 'Weather_Risk', 
        'Number_of_Stops', 'Vehicle_Age_Years', 'Warehouse_Delay_Hours', 'Priority_Numeric'
    ]
    target = 'Delivery_Time_Hours'
    
    X = df[features]
    y = df[target]
    
    # 3. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Model Training
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Model Evaluation
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Training Complete.")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f} hours")
    print(f"R-squared Score (R2): {r2:.4f}")

if __name__ == "__main__":
    main()
