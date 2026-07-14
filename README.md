# Pharmaceutical Sales Executive Dashboard

An interactive Power BI Executive Sales Dashboard designed to analyze pharmaceutical and medical supply transactions. The project covers the entire data pipeline—from raw data translation and cleaning using Python to advanced data modeling, time-intelligence calculations, and operational storytelling using DAX.

---

## Project Overview

This project simulates a real-world analytics scenario where raw transaction data is heavily restricted, poorly formatted, and presented in a foreign language. 

By utilizing **Python** for data preprocessing and translation, and **Power BI (DAX)** for business logic and visualization, a raw dataset of **75,000 transactions** was transformed into an interactive 3-page dashboard for C-level executives.

---

## The Dataset & Challenges

The initial dataset had major limitations that required extensive data engineering:
1. **Language Barrier**: The raw transactions and product names were entirely in Chinese.
2. **Limited Variables**: The dataset was exceptionally thin, containing only 7 columns: `Product Name`, `Quantity`, `Date`, `Store Name`, `Price`, `Revenue`, and `Profit`.
3. **Translation Artifacts (The Messy Data)**: 
   Translating the product names via Python introduced encoding corruptions. Leading dashes, brackets, and curly apostrophes (such as `’`, `【`, and `】`) flooded the product fields (e.g., `-Multi-di`, `【Stop mini`, `[Box]`). 
   * **The Problem**: These broken strings caused Power BI to group corrupted records under massive, meaningless blank/junk bars, completely breaking default filters and distorting "Bottom 10 Products" charts.
   * **The Fix**: Developed custom DAX filtering logic and page-level exclusions to eliminate translation artifacts, forcing the dashboard to evaluate only real, clean product names.

---

## Technical Solutions & Tech Stack

* **Data Prep & Translation**: Python (Pandas & Translation libraries) to automate translation from Chinese to English and format raw structures.
* **Feature Engineering (DAX)**: Wrote dozens of measures to squeeze deep insights from just 7 columns, calculating Year-over-Year (YoY%) changes, Month-over-Month (MoM%) growth, and dynamic store margins.
* **Advanced Filter Handling**: Integrated string matching patterns within Power BI to bypass corrupted characters and isolate actual inventory performance.

---

## Dashboard Architecture

The dashboard is structured into three distinct pages to deliver actionable business stories:

### 1. Overview (Executive Health Check)
Designed for immediate C-suite visibility into high-level performance.
* **Key Metrics**: Tracks $1.63B in Revenue, $406M in Profit, 18M Units Sold, and 75K Orders with YoY comparisons.
* **Visuals**: Trend lines for sales momentum, and structured tables highlighting the Top 5 and Bottom 5 performing stores by revenue.

### 2. Market & Store Performance (Operational Efficiency)
Focuses on individual store performance and customer purchasing behavior.
* **Key Metrics**: Tracks Average Order Value ($21.67K) and Average Items Per Invoice (241 units).
* **Visuals**: A profit-versus-orders scatter plot that immediately flags low-margin branches despite high transaction volumes.

### 3. Product Analysis (Inventory Control)
Aims at active inventory management and stock rotation.
* **Visuals**: Dynamic Treemaps showing overall product sales distribution. Features a "Top 10 Products" chart to prevent stockouts and a fully cleaned "Bottom 10 Products" chart to isolate slow-moving stock before expiry.

---

## Repository Structure

```text
├── Dataset/
│   └── translated_sales.csv       # The cleaned, translated sales data
├── Scripts/
│   └── sales.py                   # Python script used for translation and text formatting
├── pharmaceutical_sales.pbix      # The final Power BI Dashboard file
└── README.md                      # Project documentation (this file)
