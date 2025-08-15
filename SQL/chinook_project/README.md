# Chinook Music Store Database Anaylsis Project

## Project Overview
This project analyzes the Chinook database— a sample dataset representing a digital music store.  
The goal is to showcase **SQL query skills**, **data analysis**, and **visualization** techniques, producing actionable business insights.

---

## Links
- Tableau Dashboard: https://public.tableau.com/app/profile/austin.miller3996/viz/ChinookExecutiveOverview/ExecutiveOverview?publish=yes
- Source Data: https://github.com/lerocha/chinook-database

## Objectives
- Explore customer purchase behavior.
- Identify top-performing genres, artists, and tracks.
- Track revenue trends over time.
- Analyze customer retention and churn through cohort analysis.
- Prepare data for interactive Tableau dashboards.

---

## Tools & Technologies
- **SQL**: SQLite
- **Python**: Pandas, Matplotlib, Seaborn
- **Jupyter Notebook**
- **Tableau**

---

## Key Insights
- **Top Customers by Revenue**  
  Using ranking functions to find the highest-spending customers.
- **Genre Popularity**  
  Determining which genres drive the most sales.
- **Employee Performace**  
  Identifying employees who manage the most customers.
- **Daily/Monthly/Yearly Revenue Trends**  
  Tracking growth and seasonality.
- **Customer Retention & Churn**  
  Cohort-based analysis showing how customer activity changes over time.

---

## Example Visualizations
- **Top 10 Customers by Sales**
- **Revenue trends by Day of the Week**
- **Employee Performance**
- **Retention Curves by Cohort Year**

---

## Next Steps
- Publish Tableau dashboards for interactive exploration.
- Extend analysis to predictive modeling (e.g., churn prediction, sales forecasting).

---

## Project Structure
```plaintext
|--- dashboards
    |--- Chinook Executive Overview.twb
    |--- preview.png
|--- notebooks
    |--- analysis.ipynb # Main Jupyter Notebook
|--- data/ # Chinook database / CSV exports
    |--- chinook.db
    |--- [ CSV exports ]
|--- README.md # Project documentation
|--- scripts/ # SQL queries and tester, CSV generator
    |--- queries.sql
    |--- run_queries.py
    |--- csv_converter.py
```