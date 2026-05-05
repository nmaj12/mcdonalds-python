# McDonald's Data Analysis & Visualization (Python)

A Python project for analyzing and visualizing food nutrition data (e.g. McDonald’s menu) from Kaggle.  
It includes statistical analysis, clustering, regression, and an interactive Streamlit dashboard.

---

# Project Structure

- analiza.py → statistical analysis (correlation, regression, clustering, MDS projection)  
- funkcje.py → data loading, filtering, grouping pipeline  
- main.py → runs analysis and prints results  
- wizualizacje.py → Streamlit dashboard  
- menu.csv → dataset (food items from Kaggle)

---

# Features

## Data Processing
- Loading CSV data
- Filtering high-calorie products (>500 kcal)
- Grouping data by category

---

## Statistical Analysis

The project calculates:

- Average calories  
- Average calories per category  
- Correlation between fat and calories  
- Linear regression (fat → calories)

---

## Machine Learning

- KMeans clustering implemented from scratch (no sklearn)
- 2D normalization (MDS-like projection)

---

# Streamlit Dashboard

Run the application:

```bash
streamlit run wizualizacje.py
