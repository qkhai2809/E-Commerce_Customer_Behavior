import pandas as pd
from datetime import datetime
## Standardize string
def standardize_columns(df):
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df
def clean_text_col(df, columns):
    df = df.copy()
    for col in columns:
        df[col] = df[col].str.strip()
    return df
## Data type
def convert_datetime(df, columns):
    
    df = df.copy()
    for col in columns:
        if col == 'order_date':
           df[col] = pd.to_datetime(df[col], format = "%Y-%m-%d",
                                    errors="coerce")
        else:
            df[col] = pd.to_datetime(df[col], format = "%H:%M:%S",
                                                errors="coerce").dt.time

    return df
def convert_numeric(df, rules):
    df = df.copy()
    for col, type in rules.items():
        df[col] = pd.to_numeric(df[col], errors="coerce").astype(type)
    return df
## Data quality
def remove_duplicate(df):
    df = df.copy()
    df = df.drop_duplicates()
    return df
def remove_missing(df, name):
    df = df.copy()
    rules = {
        "sale":["order_id", "customer_id", "order_date", "order_status"],
        "order":["order_id", "product_id", "quantity", "unit_price"],
        "product":["product_id", "unit_price"],
        "customer": ["customer_id"]
    }
    if name in rules:
        columns = rules[name]
        df = df.dropna(subset = columns)
    return df
def remove_col(df, column):
    df = df.copy()
    for col in column:
        if col in list(df.columns):
            df.drop(columns = column, inplace = True)
    return df
## Validation
def valid(df):
    return {
        "shape" : df.shape,
        "duplicate_count" : df.duplicated().sum(),
        "missing_count" : df.isnull().sum()
    }
## Saved
def saved_file(df, path):
    df = df.copy()
    df.to_csv(path, index = False)
    print(f'File saved successfully: {path}')