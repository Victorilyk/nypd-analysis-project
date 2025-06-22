def save_report(df, output_path):
    df.to_csv(output_path, index=False)
print("Saving report to:", path)
print("Data to be saved:")
print(df.head())
