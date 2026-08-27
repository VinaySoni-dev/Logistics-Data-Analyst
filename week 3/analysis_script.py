"""
Logistics Performance Exploratory Data Analysis (EDA) Script
Week 3 Submission Package
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load shipment dataset from CSV."""
    df = pd.read_csv(filepath)
    print(f"Data successfully loaded. Shape: {df.shape}")
    return df

def perform_eda(df):
    """Perform basic exploratory data analysis and summary statistics."""
    print("\n=== DATASET OVERVIEW ===")
    print(df.info())
    
    print("\n=== MISSING VALUES ===")
    print(df.isnull().sum())
    
    df_clean = df.copy()
    df_clean['fuel_cost_inr'].fillna(df_clean['fuel_cost_inr'].median(), inplace=True)
    df_clean['delivery_time_days'].fillna(df_clean['delivery_time_days'].median(), inplace=True)
    
    print("\n=== DESCRIPTIVE STATISTICS ===")
    num_cols = ['shipment_volume_kg', 'distance_km', 'delivery_time_days', 'transport_cost_inr', 'fuel_cost_inr']
    stats = df_clean[num_cols].describe().T[['mean', '50%', 'std', 'min', 'max']]
    stats.rename(columns={'50%': 'median'}, inplace=True)
    print(stats)
    
    print("\n=== CORRELATION MATRIX ===")
    corr = df_clean[num_cols + ['on_time']].corr()
    print(corr)
    
    return df_clean

def generate_visualizations(df_clean):
    """Generate and save key logistics analysis charts."""
    sns.set_theme(style="whitegrid")
    
    plt.figure(figsize=(8, 5))
    sns.histplot(df_clean['delivery_time_days'], kde=True, color='#1f77b4', bins=20)
    plt.title('Distribution of Delivery Time (Days)')
    plt.xlabel('Delivery Time (Days)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('visualizations/delivery_time_distribution.png', dpi=300)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='transport_mode', y='transport_cost_inr', data=df_clean, palette='Set2')
    plt.title('Transportation Cost (INR) by Mode')
    plt.tight_layout()
    plt.savefig('visualizations/cost_by_transport_mode.png', dpi=300)
    plt.close()
    
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='distance_km', y='delivery_time_days', hue='transport_mode', data=df_clean, palette='bright')
    plt.title('Distance vs Delivery Time')
    plt.tight_layout()
    plt.savefig('visualizations/distance_vs_delivery_time.png', dpi=300)
    plt.close()

    print("All visualizations created and saved in 'visualizations/' directory.")

if __name__ == "__main__":
    df = load_data("logistics_data.csv")
    df_clean = perform_eda(df)
    generate_visualizations(df_clean)
