import os
from src.utils.spark_session import create_spark_session
from src.utils.logger import setup_logger
from src.utils.config import DIM_LOCATION_PATH, DIM_PROPERTY_PATH, DIM_DATE_PATH, FACT_SALES_PATH

def read_sql_file(file_path):
    """Reads a SQL file and returns the query as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def run_analytics_reports():
    """
    Executes analytical queries from external SQL files.
    """
    logger = setup_logger()
    spark = create_spark_session()
    
    logger.info("Loading modeled data and registering views...")

    # Load and Register Views
    spark.read.parquet(FACT_SALES_PATH).createOrReplaceTempView("fact_sales")
    spark.read.parquet(DIM_LOCATION_PATH).createOrReplaceTempView("dim_location")
    spark.read.parquet(DIM_PROPERTY_PATH).createOrReplaceTempView("dim_property")
    spark.read.parquet(DIM_DATE_PATH).createOrReplaceTempView("dim_date")

    # Define paths to SQL files
    sql_dir = "sql/analytics"
    queries = {
        "TOP 10 MOST EXPENSIVE CITIES": "top_expensive_cities.sql",
        "PRICE PERFORMANCE BY CATEGORY": "price_performance.sql",
        "QUARTERLY SALES VOLUME TRENDS": "sales_trends.sql"
    }

    for title, file_name in queries.items():
        logger.info(f"Running report: {title}")
        query_path = os.path.join(sql_dir, file_name)
        
        if os.path.exists(query_path):
            query = read_sql_file(query_path)
            print(f"\n--- {title} ---")
            spark.sql(query).show(truncate=False)
        else:
            logger.error(f"SQL file not found: {query_path}")

    logger.info("Analytics reports execution completed.")

if __name__ == "__main__":
    run_analytics_reports()