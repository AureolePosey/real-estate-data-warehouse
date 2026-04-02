from src.utils.spark_session import create_spark_session
from src.utils.logger import setup_logger
from src.utils.config import RAW_DATA_PATH


def ingest_data():
    logger = setup_logger()
    spark = create_spark_session()

    logger.info("Starting data ingestion...")
    
    df = (spark.read
          .option("header", "true")
          .option("inferSchema", "true")
          .csv(RAW_DATA_PATH)
    )

    logger.info("Schema of dataset:")

    df.printSchema()

    logger.info("Preview of data:")

    df.show(5)

    logger.info("Number of rows:")

    logger.info(df.count())

    return df
if __name__ == "__main__":
    ingest_data()