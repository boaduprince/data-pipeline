#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from dotenv import load_dotenv
import zipfile
import pandas as pd
import sqlalchemy as sal
from sqlalchemy import text


# 1.DOWNLOAD DATA FROM KAGGLE

from kaggle.api.kaggle_api_extended import KaggleApi

print("Downloading dataset...")

api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    "ankitbansal06/retail-orders",
    path=".",
    unzip=True
)

print("Download complete.")


# 3.LOAD DATA INTO PANDAS

print("Loading data...")

df = pd.read_csv(
    "orders.csv",
    na_values=['Not Available', 'unknown'])


# 4. DATA CLEANING (YOUR LOGIC)

# standardize column names
df.columns = df.columns.str.replace(' ', '_').str.lower()

# convert order_date if needed
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'])

# feature engineering
df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
df['sale_price'] = df['list_price'] - df['discount']
df['profit'] = df['sale_price'] - df['cost_price']

# drop unnecessary columns
df = df.drop(columns=['list_price', 'cost_price', 'discount_percent'])

print("Cleaning complete.")

# 5. CONNECT TO MYSQL
print("Connecting to MySQL...")

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

connection = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = sal.create_engine(connection)

with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE orders"))
    conn.commit()

# 6. LOAD DATA INTO MYSQL
print("Loading data into MySQL...")

df.to_sql(
    name='orders',
    con=engine,
    if_exists='append',
    index=False
)

print("PIPELINE COMPLETED SUCCESSFULLY")
 
df = pd.read_sql("select * from order", con =engine)
df.head(5)
