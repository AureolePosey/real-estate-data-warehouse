import sys
from src.utils.logger import setup_logger
# Vérifie bien ces noms de fonctions (après le 'import')
from src.ingestion.ingest_data import ingest_data 
from src.cleaning.clean_data import clean_data
from src.transformation.transform_data import transform_data
from src.modeling.model_data import create_star_schema
from src.analytics.reports import run_analytics_reports

def run_pipeline():
    logger = setup_logger()
    logger.info("Starting Full Data Warehouse Pipeline...")

    try:
        logger.info("Step 1: Ingestion...")
        ingest_data()

        logger.info("Step 2: Cleaning...")
        clean_data()

        logger.info("Step 3: Transformation...")
        transform_data()

        logger.info("Step 4: Modeling...")
        create_star_schema()

        logger.info("Step 5: Analytics Reports...")
        run_analytics_reports()

        logger.info("Full Pipeline Completed Successfully!")

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()