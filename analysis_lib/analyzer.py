import pandas as pd

def analyze_data(data):
    """
    Combine input datasets and calculate key metrics:
    - Population density (people per km²)
    - Fire rate (fires per 100,000 people)
    - Alcohol seller rate (sellers per 100,000 people)
    """
    print("Keys received:", list(data.keys()))
    for name, df in data.items():
        print(f"{name}.shape:", df.shape)
        print(df['region'].head())

    population_df = data['population'].copy()
    area_df = data['area'].copy()
    fires_df = data['fires'].copy()
    alcohol_df = data['alcohol'].copy()

    for df_ in [population_df, area_df, fires_df, alcohol_df]:
        df_['region'] = df_['region'].str.strip().str.lower()

    df = population_df.merge(area_df, on='region', how='inner')
    df = df.merge(fires_df, on='region', how='inner')
    df = df.merge(alcohol_df, on='region', how='inner')

    df['density'] = (df['population'] / df['area']).round(2)
    df['fire_rate'] = (df['fire_count'] / df['population'] * 100000).round(2)
    df['alcohol_rate'] = (df['alcohol_sellers'] / df['population'] * 100000).round(2)

    print("\nAfter merging and calculating:")
    print(df.head())

    return df

def calculate_basic_statistics(df):
    return df.describe()

def calculate_correlation(df1, df2, join_column, col1, col2):
    merged = df1.merge(df2, on=join_column)
    return merged[col1].corr(merged[col2])
