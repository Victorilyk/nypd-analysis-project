from analysis_lib import data_loader, data_cleaner

data = data_loader.load_csv_files_from_directory("my_data")

for name, df in data.items():
    print(f"\n{name.upper()} — missing values per column:")
    print(data_cleaner.check_missing_values(df))
