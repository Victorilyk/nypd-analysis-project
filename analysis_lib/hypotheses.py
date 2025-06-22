import pandas as pd

def analyze_hypotheses(df):
    print("\nHypothesis 1: Population vs Fire Events")
    try:
        corr1 = df['population'].corr(df['fire_count'])
        print(f"Correlation: {corr1:.4f}")
    except Exception as e:
        print(f"Failed: {e}")

    print("\nHypothesis 2: Population vs Alcohol Selling Points")
    try:
        corr2 = df['population'].corr(df['alcohol_sellers'])
        print(f"Correlation: {corr2:.4f}")
    except Exception as e:
        print(f"Failed: {e}")

    print("\nHypothesis 3: Alcohol Selling Points vs Fire Events")
    try:
        corr3 = df['alcohol_sellers'].corr(df['fire_count'])
        print(f"Correlation: {corr3:.4f}")
    except Exception as e:
        print(f"Failed: {e}")

    print("\nHypothesis 4: Population Density vs Fire Rate (fires per 1000 people)")
    try:
        df['density'] = pd.to_numeric(df['density'], errors='coerce')
        df['fire_rate'] = pd.to_numeric(df['fire_rate'], errors='coerce')
        corr4 = df['density'].corr(df['fire_rate'])
        print(f"Correlation: {corr4:.4f}")
    except Exception as e:
        print(f"Failed: {e}")
