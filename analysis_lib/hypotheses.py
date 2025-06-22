def analyze_hypotheses(df):
    print("Hypothesis 1: Population vs Fire Events")
    corr1 = df['population'].corr(df['fires'])
    print(f"Correlation: {corr1:.2f}")

    print("Hypothesis 2: Population vs Alcohol Selling Points")
    corr2 = df['population'].corr(df['alcohol_points'])
    print(f"Correlation: {corr2:.2f}")

    print("Hypothesis 3: Alcohol Selling Points vs Fire Events")
    corr3 = df['alcohol_points'].corr(df['fires'])
    print(f"Correlation: {corr3:.2f}")

    # Additional hypothesis: Urban vs Rural fire events per capita
    if 'region_type' in df.columns:
        print("Hypothesis 4: Urban areas have more fire events per capita than rural areas")
        urban = df[df['region_type'] == 'urban']
        rural = df[df['region_type'] == 'rural']

        urban_rate = (urban['fires'] / urban['population']).mean()
        rural_rate = (rural['fires'] / rural['population']).mean()

        print(f"Urban fire rate per capita: {urban_rate:.4f}")
        print(f"Rural fire rate per capita: {rural_rate:.4f}")
    else:
        print("Column 'region_type' not found — cannot evaluate Hypothesis 4")
