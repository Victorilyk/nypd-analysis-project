import pandas as pd

def clean_data(data_dict):
    """
    Basic data cleaning:
    - Drop fully empty rows
    - Strip whitespace from 'region' column if it exists
    """
    cleaned_data = {}

    for name, df in data_dict.items():
        df = df.dropna(how="all")
        if 'region' in df.columns:
            df['region'] = df['region'].str.strip()
        cleaned_data[name] = df

    return cleaned_data


def check_missing_values(df):
    """
    Return a Series with the count of missing values per column.
    """
    return df.isnull().sum()


def clean_dataframe(df, drop_threshold=0.5):
    """
    Cleans a DataFrame by:
    - Dropping columns with more than `drop_threshold` proportion of missing values
    - Dropping rows with any missing values

    Returns:
    - Cleaned DataFrame
    - Dictionary with info on dropped columns and rows
    """
    info = {}
    
    # Identify columns to drop
    missing_ratio = df.isnull().mean()
    columns_to_drop = missing_ratio[missing_ratio > drop_threshold].index.tolist()
    
    # Drop those columns
    df = df.drop(columns=columns_to_drop)
    
    # Count rows to drop
    rows_before = df.shape[0]
    df = df.dropna()
    rows_after = df.shape[0]
    
    # Prepare info
    info['dropped_columns'] = columns_to_drop
    info['dropped_rows'] = rows_before - rows_after

    return df, info
