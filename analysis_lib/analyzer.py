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

    population_df = data['population']
    area_df = data['area']
    fires_df = data['fires']
    alcohol_df = data['alcohol']

    df = population_df.merge(area_df, on='region')
    df = df.merge(fires_df, on='region')
    df = df.merge(alcohol_df, on='region')

    df['density'] = (df['population'] / df['area']).round(2)
    df['fire_rate'] = (df['fire_count'] / df['population'] * 100000).round(2)
    df['alcohol_rate'] = (df['alcohol_sellers'] / df['population'] * 100000).round(2)

    print("➡ After merging and calculating:")
    print(df.head())

    return df
