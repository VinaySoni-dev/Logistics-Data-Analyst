# Logistics & Supply Chain EDA - Week 3 Project

## Overview
This repository contains the complete Week 3 analytical deliverable focusing on **Logistics Performance Analysis and Operational Bottleneck Diagnostics**. The study analyzes a dataset of 250 domestic freight shipments across multiple transport modes and regional hubs.

## Repository Structure
```
logistics-eda-week3/
│
├── Week3_Logistics_Performance_Report.docx   # Comprehensive executive report
├── logistics_data.csv                       # Dataset (250 shipment records)
├── analysis_script.py                       # Modular Python analysis script
├── notebook.ipynb                           # Interactive Jupyter Notebook
├── WEEK3_SUBMISSION_DESCRIPTION.md          # Project summary & narrative
├── README.md                                # Project documentation
│
└── visualizations/                          # Generated high-res charts
    ├── delivery_time_distribution.png
    ├── cost_by_transport_mode.png
    ├── distance_vs_delivery_time.png
    ├── regional_on_time_performance.png
    └── correlation_matrix.png
```

## Setup & Running the Analysis

### Requirements
- Python 3.8+
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `python-docx`

### Quick Start
1. Clone repository:
   ```bash
   git clone https://github.com/your-username/logistics-eda-week3.git
   cd logistics-eda-week3
   ```
2. Run automated analysis script:
   ```bash
   python analysis_script.py
   ```
3. Open Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

## Key Findings Summary
- **Primary Cost Driver**: Transport costs are heavily dominated by Air freight (median ~₹22,500), strongly driven by fuel expenditure (r = 0.84).
- **Bottlenecks**: Road shipments over 1,200 km experience severe schedule decay. The East region trails in on-time delivery compliance (~65%).
- **Optimization Strategy**: Transition long-haul road transport to Rail-Road intermodal routes to reduce freight cost by ~22%.

---
*Created as part of Week 3 Submission Package.*
