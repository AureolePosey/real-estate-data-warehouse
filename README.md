 REAL ESTATE DATA WAREHOUSE — DATA ENGINEERING PIPELINE


🎯 PROJECT OVERVIEW

        This project is an end-to-end Data Engineering pipeline built with PySpark.

        The objective is to transform raw and unstructured real estate data into a scalable and analytics-ready Data Warehouse, enabling business users to analyze market trends, identify high-value locations, and monitor price evolution over time.

💼 Business Context

        Real estate analysts need reliable and structured data to:

        Identify the most profitable cities
        Track price evolution over time
        Compare property types (size, category, etc.)
        Support investment decision-making

        Raw CSV files are often inconsistent, slow to query, and not suitable for analytics.

👉 This project solves that by building a clean, optimized, and structured data model.

🏗️ ARCHITECTURE

    The pipeline follows a Medallion-like architecture:

        *Ingestion
            -Load raw CSV data into Spark

        *Cleaning
            -Handle missing values
            -Fix data types
            -Remove duplicates

        *Transformation (Curated Layer)
            -Feature engineering (price per sqft, categories)
            -Time enrichment (year, month, quarter)

        *Data Modeling (Star Schema)
            -Fact table: fact_sales
            -Dimensions: dim_location, dim_property, dim_date

        *Analytics Layer
            -Business queries written in SQL
            -Decoupled from Python logic
⚙️ TECH STACK
        -PySpark
        -SQL
        -Parquet
        -Data Modeling (Star Schema)
        -Logging


📁 Project Structure
        .
        ├── data/                   
        ├── sql/
        │   └── analytics/          
        ├── src/
        │   ├── ingestion/          
        │   ├── cleaning/           
        │   ├── transformation/     
        │   ├── modeling/           
        │   ├── analytics/          
        │   └── utils/              
        └── main.py  



*Key Insights Generated
        -Top cities by price
        -Price per sqft analysis
        -Market segmentation by property size
        -Quarterly sales trends

*Key Learnings
        -Designing scalable data pipelines with PySpark
        -Structuring data for analytics using Star Schema
        -Separating engineering logic from business queries
        -Handling large datasets (2M+ rows) efficiently


*Next Steps
        -Add orchestration with Apache Airflow
        -Automate pipeline scheduling
        -Improve monitoring and alerting