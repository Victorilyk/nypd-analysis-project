import pandas as pd
from analysis_lib.data_cleaner import check_missing_values, clean_dataframe

def test_check_missing_values():
    df = pd.DataFrame({
        'A': [1, None, 3],
        'B': [4, 5, 6]
    })
    result = check_missing_values(df)
    assert result['A'] == 1
    assert result['B'] == 0

def test_clean_dataframe():
    df = pd.DataFrame({
        'A': [1, None, 3],
        'B': [None, None, 6]
    })
    cleaned_df, info = clean_dataframe(df, drop_threshold=0.5)
    assert 'B' in info['dropped_columns']
    assert info['dropped_rows'] >= 0
    assert isinstance(cleaned_df, pd.DataFrame)
