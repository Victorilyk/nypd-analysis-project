def save_report(df, output_path):
    df.to_csv(output_path, index=False)
