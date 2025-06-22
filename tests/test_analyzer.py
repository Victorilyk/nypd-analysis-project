import pandas as pd
from analysis_lib.analyzer import calculate_basic_statistics, calculate_correlation

def test_calculate_basic_statistics():
    df = pd.DataFrame({
        'X': [1, 2, 3, 4, 5],
        'Y': [10, 20, 30, 40, 50]
    })
    stats = calculate_basic_statistics(df)
    assert 'X' in stats.columns
    assert 'mean' in stats.index
    assert round(stats.loc['mean', 'Y']) == 30

def test_calculate_correlation():
    df1 = pd.DataFrame({
        'region': ['A', 'B', 'C'],
        'pop': [1000, 2000, 3000]
    })
    df2 = pd.DataFrame({
        'region': ['A', 'B', 'C'],
        'fires': [10, 20, 30]
    })
    corr = calculate_correlation(df1, df2, 'region', 'pop', 'fires')
    assert round(corr, 2) == 1.0
