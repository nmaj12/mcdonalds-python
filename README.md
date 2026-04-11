# 🍔 McDonald's Data Analysis & Visualization (Python)

A Python project for analyzing and visualizing food nutrition data (e.g. McDonald’s menu) from Kaggle.  
It includes statistical analysis, clustering, regression, and an interactive Streamlit dashboard.

---

# 📁 Project Structure

- analiza.py → statistical analysis (correlation, regression, clustering, MDS projection)  
- funkcje.py → data loading, filtering, grouping pipeline  
- main.py → runs analysis and prints results  
- wizualizacje.py → Streamlit dashboard  
- menu.csv → dataset (food items from Kaggle)

---

# 📊 Features

## 📌 Data Processing
- Loading CSV data
- Filtering high-calorie products (>500 kcal)
- Grouping data by category

---

## 📈 Statistical Analysis

The project calculates:

- Average calories  
- Average calories per category  
- Correlation between fat and calories  
- Linear regression (fat → calories)

---

## 🤖 Machine Learning

- KMeans clustering implemented from scratch (no sklearn)
- 2D normalization (MDS-like projection)

---

# 📊 Streamlit Dashboard

Run the application:

streamlit run wizualizacje.py

---

## 🎛 Dashboard Features

- Interactive data table
- Category filtering
- Multiple visualization types:
  - Streamlit built-in charts
  - Matplotlib
  - Seaborn
  - Plotly
  - Altair

---

# 🧠 Skills Demonstrated

- Data analysis in Python
- Data visualization
- Functional programming (pipeline & composition)
- Statistical analysis (correlation, regression)
- Basic machine learning (clustering)
- Building interactive dashboards with Streamlit

---

# ⭐ About This Project

This project was created to practice:
data analysis, visualization, and basic machine learning in Python using real-world dataset from Kaggle.
