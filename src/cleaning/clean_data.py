from src.utils.spark_session import create_spark_session
from src.utils.logger import setup_logger
from src.utils.config import RAW_DATA_PATH, CLEANED_DATA_PATH
from pyspark.sql import functions as F


def clean_data():
    logger = setup_logger()
    spark = create_spark_session()

    logger.info("Starting data cleaning...")

    df = (spark.read
          .option("header", "true")
          .option("inferSchema", "true")
          .csv(RAW_DATA_PATH)
    )

    #count total rows    
    total_rows = df.count()
    logger.info(f"Total rows in dataset: {total_rows}")

    # count missing values
    missing_counts = df.select([F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns])
    logger.info("Missing values count:")
    missing_counts.show()


    #drop street column and brokered_by column
    df_cleaned = df.drop("street", "brokered_by")
    logger.info("Dropped 'street' and 'brokered_by' columns.")

    #redefine zip_code as string
    df_cleaned = (df_cleaned.withColumn("zip_code", F.col("zip_code").cast("string")))
    

    #filter price column and city column where is not null
    df_cleaned = df_cleaned.filter((F.col("price").isNotNull()) & (F.col("city").isNotNull()))
    


    #Add sale_date to df
    df_cleaned = df_cleaned.withColumn("sale_date", 
        F.when(F.col("prev_sold_date").isNotNull(), F.add_months(F.col("prev_sold_date"), 12))
         .otherwise(F.to_date(F.lit("2024-01-01"))),
         
    )

    #create flag for simulated sale date
    df_cleaned = df_cleaned.withColumn("is_simulated_date", 
        F.when(F.col("prev_sold_date").isNull(), F.lit(True)).otherwise(F.lit(False))
    )

    #drop duplicate rows based on all columns
    df_cleaned = df_cleaned.dropDuplicates(["city", "price", "house_size", "state"])
    

    #final count of rows after cleaning
    final_rows = df_cleaned.count()
    logger.info(f"Total rows after cleaning: {final_rows}")

    #% of rows dropped
    percent_dropped = ((total_rows - final_rows) / total_rows) * 100
    logger.info(f"Percentage of rows dropped: {percent_dropped:.2f}%")

    #log final schema and preview of cleaned data
    logger.info("Schema of cleaned dataset:")
    df_cleaned.printSchema()
    logger.info("Preview of cleaned dataset:")
    df_cleaned.show()

    logger.info("Data cleaning completed.")

    return df_cleaned
if __name__ == "__main__":    
    # use logger to log the cleaning process and results
    logger = setup_logger() 
    
    #start cleaning data
    cleaned_df = clean_data()

    #save cleaned data to parquet file
    cleaned_df.write \
        .mode("overwrite") \
        .parquet(CLEANED_DATA_PATH)
    
    logger.info(f"Cleaned data saved to '{CLEANED_DATA_PATH}'")