import os
import pandas as pd

def load_csv_files_from_directory(directory_path):
    data = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory_path, filename)
            key = os.path.splitext(filename)[0]
            df = pd.read_csv(filepath)
            data[key] = df
    return data
def load_csv(path):
    return pd.read_csv(path)
