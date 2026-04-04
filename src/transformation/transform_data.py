from src.utils.spark_session import create_spark_session
from src.utils.logger import setup_logger
from src.utils.config import CLEANED_DATA_PATH, CURATED_DATA_PATH
from pyspark.sql import functions as F


def transform_data():
    logger = setup_logger()
    spark = create_spark_session()

    logger.info("Starting data transformation...")

    df_cleaned = spark.read.parquet(CLEANED_DATA_PATH)

    # create all new columns in one go to avoid multiple transformations

    df_transformed = df_cleaned.withColumn(
        "price_per_sqft", 
        F.round(F.when(F.col("house_size") > 0, F.col("price") / F.col("house_size")).otherwise(None), 2)
    ).withColumn(
        "property_size_category",
        F.when(F.col("house_size") < 1000, "SMALL")
         .when((F.col("house_size") >= 1000) & (F.col("house_size") < 3000), "MEDIUM") 
         .when(F.col("house_size") >= 3000, "LARGE")
         .otherwise("UNKNOWN")
    ).withColumn(
        "sale_year", F.year("sale_date")
    ).withColumn(
        "sale_month", F.month("sale_date")
    ).withColumn(
        "sale_quarter", F.quarter("sale_date")
    )


    
    # Log the average price per sqft by property size category for validation
    logger.info("Final validation : Average price per sqft by property size category:")
    df_transformed.groupBy("property_size_category").agg(
        F.round(F.avg("price_per_sqft"), 2).alias("avg_price_per_sqft")).show()
    return df_transformed

if __name__ == "__main__":
    

    #use logger
    logger = setup_logger()
    df_transformed = transform_data()
    logger.info("Data transformation completed. Saving transformed data to Parquet...")
    #save transformed data to parquet
    df_transformed.write.mode("overwrite").parquet(CURATED_DATA_PATH)

    logger.info("Process finished successfully.")