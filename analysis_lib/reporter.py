import pandas as pd

def save_report(df: pd.DataFrame, filename: str):
    name = filename.replace('.csv', '')

    if isinstance(df, pd.DataFrame):
        print(f"{name.upper()}: {list(df.columns)}")
    elif isinstance(df, pd.Series):
        print(f"{name.upper()}: Series with name: {df.name}")
    else:
        print(f"{name.upper()}: Unknown type: {type(df)}")

def save_report(dataframe, output_path):
    dataframe.to_csv(output_path, index=False, encoding="utf-8", sep=";")


