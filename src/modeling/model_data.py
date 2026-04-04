from src.utils.spark_session import create_spark_session
from src.utils.logger import setup_logger
from src.utils.config import CURATED_DATA_PATH, DIM_LOCATION_PATH, DIM_PROPERTY_PATH, DIM_DATE_PATH, FACT_SALES_PATH
from pyspark.sql import functions as F
from pyspark.sql import Window

def create_star_schema():
    logger = setup_logger()
    spark = create_spark_session()
    
    logger.info("Starting dimension creation...")
    df_curated = spark.read.parquet(CURATED_DATA_PATH)

    # --- secure joins for null values ---
    fill_values = {
        "city": "UNKNOWN", "state": "UNKNOWN", "zip_code": 0,
        "status": "UNKNOWN", "bed": 0, "bath": 0, "acre_lot": 0.0,
        "house_size": 0.0, "property_size_category": "UNKNOWN"
    }
    df_curated = df_curated.fillna(fill_values)

    # --- Window specs for stable IDs ---
    w_loc = Window.orderBy("state", "city", "zip_code")
    w_prop = Window.orderBy("status", "bed", "bath", "property_size_category")
    w_date = Window.orderBy("sale_date")

    # Create dim_location
    dim_location = df_curated.select("city", "state", "zip_code").distinct() \
                             .withColumn("location_id", F.row_number().over(w_loc))
    dim_location.write.mode("overwrite").parquet(DIM_LOCATION_PATH)
    logger.info("Dimension 'dim_location' created and saved.")
    dim_location.show(10, truncate=False)

    # Create dim_property 
    dim_property = df_curated.select("status", "bed", "bath", "property_size_category").distinct() \
                             .withColumn("property_id", F.row_number().over(w_prop))
    dim_property.write.mode("overwrite").parquet(DIM_PROPERTY_PATH)
    logger.info("Dimension 'dim_property' created and saved.")
    dim_property.show(10, truncate=False)

    # Create dim_date 
    dim_date = df_curated.select("sale_date","sale_year","sale_month","sale_quarter").distinct() \
                         .withColumn("date_id", F.row_number().over(w_date))
    dim_date.write.mode("overwrite").parquet(DIM_DATE_PATH)
    logger.info("Dimension 'dim_date' created and saved.")
    dim_date.show(10, truncate=False)

    # Create fact_sales
    # first join with dim_location
    fact_sales = df_curated.join(dim_location, on=["city", "state", "zip_code"], how="left") 

    # second join with dim_property 
    fact_sales = fact_sales.join(dim_property, on=["status", "bed", "bath", "property_size_category"], how="left")

    # third join with dim_date
    fact_sales = fact_sales.join(dim_date, on=["sale_date"], how="left")

    # select only required columns for fact_sales 
    fact_sales = fact_sales.select(
        "location_id", 
        "property_id", 
        "date_id", 
        "price", 
        "house_size", 
        "acre_lot", 
        "price_per_sqft"
    )
    fact_sales.write.mode("overwrite").parquet(FACT_SALES_PATH)
    logger.info("Fact table 'fact_sales' created and saved.")
    fact_sales.show(10, truncate=False)

if __name__ == "__main__":
    create_star_schema()