 Data Pipeline Project

 Overview

This project is an end-to-end automated data pipeline that extracts data from the Kaggle API, transforms it, and loads it into a MySQL database.

The pipeline is fully automated from data acquisition to database storage.



* Python
* Pandas
* Kaggle API
* SQL (MySQL)
* SQLAlchemy



1. Extract (Kaggle API)

   * Data is automatically downloaded from Kaggle using the Kaggle API
   * Raw dataset is stored locally in the project directory

2. Transform

   * Data cleaning (handling missing values, duplicates)
   * Feature engineering and formatting

3. Load

   * Processed data is loaded into a MySQL database
   * Tables are updated for analysis and reporting


HOW TO RUN
python pipeline.py


 Key Feature

* Fully automated ETL pipeline
* Direct data ingestion from Kaggle API
* Scalable structure for future data sources
