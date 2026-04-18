#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import zipfile
import pandas as pd
import sqlalchemy as sal
from sqlalchemy import text


# 1.DOWNLOAD DATA FROM KAGGLE

print("Downloading dataset...")

os.system("kaggle datasets download ankitbansal06/retail-orders -f orders.csv")

print("Download complete.")


# 2.UNZIP FILE

print("Unzipping file...")

zip_ref = zipfile.ZipFile("orders.csv.zip")
zip_ref.extractall()
zip_ref.close()

print("Unzipping complete.")


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

engine = sal.create_engine(
    "mysql+pymysql://newuser:camry2017@localhost/order_db")

with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE orders"))

# 6. LOAD DATA INTO MYSQL
print("Loading data into MySQL...")

df.to_sql(
    name='orders',
    con=engine,
    if_exists='append',
    index=False
)

print("PIPELINE COMPLETED SUCCESSFULLY")
