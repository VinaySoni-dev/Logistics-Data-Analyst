# YUVA Internship – Logistics Data Analysis

## Week 1: Strategic Planning and Data Exploration in Logistics

This repository contains the Week 1 work for a YUVA internship focused on applying Python and data science techniques to logistics and supply-chain problems.

### Project Scenario

The project studies an e-commerce logistics operation where orders are fulfilled by multiple sellers and delivered to customers across different geographic regions. The objective is to understand delivery performance, freight cost, customer satisfaction, and operational patterns using historical data.

### Objectives

- Explore historical logistics and e-commerce data.
- Calculate important logistics KPIs.
- Identify factors associated with late deliveries.
- Analyze delivery time and freight-cost patterns.
- Prepare features for predictive modelling.
- Explore seller segmentation using clustering.
- Define a future Vehicle Routing Problem (VRP) optimization approach.

### Key KPIs

| KPI | Purpose |
|---|---|
| On-Time Delivery Rate | Measures delivery reliability |
| Average Delivery Lead Time | Measures delivery speed |
| Late Delivery Rate | Identifies service failures |
| Average Freight Cost per Order | Tracks transportation cost |
| Average Review Score | Connects logistics with customer satisfaction |
| Orders per Seller | Shows seller workload/concentration |

### Dataset

The proposed project uses the **Brazilian E-Commerce Public Dataset by Olist**, a public dataset containing approximately 100,000 orders and related information about customers, sellers, products, order items, payments, reviews, and geolocation.

Dataset source:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset itself is not included in this repository. Download it from the source above and place the CSV files inside the `data/` directory.

### Project Roadmap

```text
Data Collection
      ↓
Data Validation
      ↓
Data Cleaning
      ↓
Data Integration
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
KPI Analysis
      ↓
Predictive Modelling
      ↓
Seller/Region Clustering
      ↓
Route Optimization Prototype
      ↓
Evaluation
      ↓
Business Recommendations
```

### Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google OR-Tools
- Jupyter Notebook

### Repository Structure

```text
yuva-logistics-data-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── week1_logistics_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── kpi_analysis.py
│   ├── exploratory_analysis.py
│   └── modeling.py
│
├── reports/
│   └── Week1_Logistics_Strategic_Planning_Report.docx
│
└── outputs/
    └── .gitkeep
```

### How to Run

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download the Olist dataset.
5. Place the CSV files in `data/`.
6. Open the notebook:

```bash
jupyter notebook
```

7. Run `notebooks/week1_logistics_analysis.ipynb`.

### Week 1 Status

- [x] Project definition
- [x] Logistics scenario
- [x] KPI identification
- [x] Dataset selection
- [x] Data science methodology planning
- [x] Analysis roadmap
- [x] Python starter code
- [ ] Full dataset analysis
- [ ] Predictive model evaluation
- [ ] Clustering results
- [ ] Route optimization results

### References

- Olist Brazilian E-Commerce Dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- World Bank Logistics Performance Index: https://data.worldbank.org/indicator/LP.LPI.OVRL.XQ
- Google OR-Tools: https://developers.google.com/optimization/routing
- Scikit-learn: https://scikit-learn.org/

## Author

**Vinay Soni**

YUVA Internship – Week 1


## Week 2 – Data Cleaning and Preprocessing

Week 2 extends the strategic plan into a reproducible data-preparation workflow.

### Week 2 Work

- Data collection simulation using the Olist public dataset
- Data-quality profiling
- Missing-value analysis and treatment strategy
- Duplicate detection
- Date/time standardization
- Categorical normalization
- IQR-based outlier detection
- Min-Max normalization
- StandardScaler standardization
- Logistics feature engineering
- Post-cleaning validation

### Week 2 Notebook

`notebooks/week2_data_cleaning_preprocessing.ipynb`

### Week 2 Report

`reports/YUVA_Internship_Week_2_Data_Cleaning_Preprocessing_Report.docx`
