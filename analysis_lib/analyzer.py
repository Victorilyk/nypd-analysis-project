import pandas as pd

def analyze_data(data):
    """
    Combine input datasets and calculate key metrics:
    - Population density (people per km²)
    - Fire rate (fires per 100,000 people)
    - Alcohol seller rate (sellers per 100,000 people)
    """

    # Get individual DataFrames
    population_df = data['population']
    area_df = data['area']
    fires_df = data['fires']
    alcohol_df = data['alcohol']

    # Merge all datasets by 'region'
    df = population_df.merge(area_df, on='region')
    df = df.merge(fires_df, on='region')
    df = df.merge(alcohol_df, on='region')

    # Calculate population density
    df['density'] = (df['population'] / df['area']).round(2)

    # Calculate fire rate per 100,000 population
    df['fire_rate'] = (df['fire_count'] / df['population'] * 100000).round(2)

    # Calculate alcohol seller rate per 100,000 population
    df['alcohol_rate'] = (df['alcohol_sellers'] / df['population'] * 100000).round(2)

    return df
    print("Merged dataset columns:", result_df.columns)
    print("Shape of result:", result_df.shape)
    print(result_df.head())

