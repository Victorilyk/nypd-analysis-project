import pandas as pd

def save_report(df: pd.DataFrame, filename: str):
    name = filename.replace('.csv', '')

    if isinstance(df, pd.DataFrame):
        print(f"{name.upper()}: {list(df.columns)}")
    elif isinstance(df, pd.Series):
        print(f"{name.upper()}: Series with name: {df.name}")
    else:
        print(f"{name.upper()}: Unknown type: {type(df)}")

    df.to_csv(filename, index=False)
