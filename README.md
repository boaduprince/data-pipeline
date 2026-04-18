 Data Pipeline Project (ETL with Python, Kaggle API & MySQL)

# Overview

This project is an end-to-end **ETL (Extract, Transform, Load) data pipeline** that automates the process of collecting data from the Kaggle API, cleaning and transforming it using Python, and loading it into a MySQL database for storage and analysis.

The goal of this project is to simulate a real-world data engineering workflow and demonstrate skills in data extraction, transformation, and database integration.

Tools & Technologies

* Python
* Pandas
* SQLAlchemy
* MySQL
* Kaggle API
* Jupyter Notebook (for development & testing)

---

# Pipeline Workflow

# 1. Extract

* Data is automatically fetched from Kaggle using the Kaggle API
* Dataset is downloaded and loaded into a Pandas DataFrame

# 2. Transform

* Data cleaning (handling missing values, correcting formats)
* Feature engineering and preparation
* Structuring data for database storage

# 3. Load

* Cleaned data is loaded into a MySQL database using SQLAlchemy
* Existing table is truncated before inserting new data
* Uses SQLAlchemy `text()` for executing raw SQL commands


---

# How to Run the Pipeline

1. Ensure you have Python installed and required packages:

```bash
pip install pandas sqlalchemy pymysql kaggle
```

2. Set up your Kaggle API credentials:

* Place your `kaggle.json` file in the correct directory

3. Configure your MySQL database connection in your script or environment variables

4. Run the pipeline:

```bash
python pipeline.py
```
---
