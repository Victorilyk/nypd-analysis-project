def save_report(df, output_path):
    print("Saving report to:", output_path)
    print("Data to be saved:")
    print(df.head())
    df.to_csv(output_path, index=False)
