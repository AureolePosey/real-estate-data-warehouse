Markdown
# 🏠 Real Estate Data Warehouse — Data Engineering Pipeline

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-3.5.0-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

## 🎯 Project Overview
This project is an end-to-end **Data Engineering pipeline** built with **PySpark**. 

The objective is to transform raw, unstructured real estate data into a scalable and analytics-ready **Data Warehouse**. It enables business users to analyze market trends, identify high-value locations, and monitor price evolution over time.

### 💼 Business Context
Real estate analysts need reliable and structured data to:
*   Identify the most profitable cities.
*   Track price evolution over time.
*   Compare property types (size, category, etc.).
*   Support investment decision-making.

> **Problem:** Raw CSV files are often inconsistent, slow to query, and not suitable for complex analytics.
> **Solution:** This pipeline builds a clean, optimized, and structured **Star Schema** data model.

---

## 🏗️ Architecture & Data Flow
The pipeline follows a **Medallion-like architecture**:

1.  **Ingestion**: Load raw CSV data into Spark DataFrames.
2.  **Cleaning**: Handle missing values, fix data types, and remove duplicates.
3.  **Transformation (Curated Layer)**: Feature engineering (price per sqft, size categories) and time enrichment.
4.  **Data Modeling (Star Schema)**: Implementation of `fact_sales`, `dim_location`, `dim_property`, and `dim_date`.
5.  **Analytics Layer**: Business queries written in SQL, decoupled from Python logic.

---

## 📊 Sample Results & Analytics
*A recruteur wants to see the output. Here is what the pipeline produces:*

### 1. Top 10 Most Expensive Cities
Analysis of average property prices across different states and cities.
| state | city | avg_price | sales_volume |
| :--- | :--- | :--- | :--- |
| Kansas | Eureka | 5.01E7 | 20 |
| Illinois | Wayne City | 4.33E7 | 3 |
| Florida | Manalapan | 2.47E7 | 18 |

### 2. Price Performance by Category
Segmentation of the market by property size (Small, Medium, Large).
| property_size_category | avg_sqft_price | avg_house_size |
| :--- | :--- | :--- |
| **SMALL** | 387.92 | 806.38 |
| **LARGE** | 317.80 | 9659.20 |
| **MEDIUM** | 260.28 | 1799.01 |

---

## 🚀 How to Run

### Prerequisites
*   Python 3.8+
*   Apache Spark 3.x
*   Java 8 or 11

### Installation & Execution
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/AureolePosey/real-estate-data-warehouse.git](https://github.com/AureolePosey/real-estate-data-warehouse.git)
   cd real-estate-data-warehouse
Install dependencies:

Bash
pip install -r requirements.txt
Run the pipeline:

Bash
python3 main.py
📁 Project Structure
Plaintext
.
├── data/               # Raw, Cleaned, Curated, and Modeled (Parquet)
├── sql/                # Decoupled SQL queries for analytics
│   └── analytics/
├── src/                # Modular Python source code
│   ├── ingestion/      # Data loading logic
│   ├── cleaning/       # Data quality & type casting
│   ├── transformation/ # Feature engineering
│   ├── modeling/       # Star Schema creation
│   └── analytics/      # SQL execution engine
├── main.py             # Pipeline entry point (Orchestrator)
└── pipeline.log        # Execution logs
🧠 Key Learnings
Scalability: Designing pipelines capable of handling large datasets (2M+ rows) efficiently.

Modularity: Separating engineering logic (Python) from business logic (SQL).

Data Quality: Implementing robust cleaning and validation steps.

Storage: Utilizing Parquet format for optimized storage and fast analytical queries.

🚀 Next Steps
[ ] Add orchestration with Apache Airflow.

[ ] Containerize the environment with Docker.

[ ] Implement Data Quality tests with Great Expectations.