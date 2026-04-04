import os
RAW_DATA_PATH = "data/raw/realtor-data.zip.csv"
CLEANED_DATA_PATH = "data/cleaned/cleaned_data.parquet"
CURATED_DATA_PATH = "data/curated/curated_data.parquet"

#new path for data modeling
MODELING_PATH = os.path.join("data", "modeling")
DIM_LOCATION_PATH = os.path.join(MODELING_PATH, "dim_location")
DIM_PROPERTY_PATH = os.path.join(MODELING_PATH, "dim_property")
DIM_DATE_PATH = os.path.join(MODELING_PATH, "dim_date")
FACT_SALES_PATH = os.path.join(MODELING_PATH, "fact_sales")
