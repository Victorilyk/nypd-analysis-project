def clean_data(data_dict):
    """
    Basic data cleaning:
    - Drop fully empty rows
    - Strip whitespace from 'region' column if it exists
    """
    cleaned_data = {}

    for name, df in data_dict.items():
        # Drop completely empty rows
        df = df.dropna(how="all")

        # Strip whitespace from 'region' column
        if 'region' in df.columns:
            df['region'] = df['region'].str.strip()

        cleaned_data[name] = df

    return cleaned_data


def check_missing_values(df):
    return df.isnull().sum()


def clean_dataframe(df):
    return df.dropna()
