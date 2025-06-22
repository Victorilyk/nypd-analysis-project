import argparse
import os
from analysis_lib import data_loader, data_cleaner, analyzer, reporter
from analysis_lib.hypotheses import analyze_hypotheses  

def main():
    parser = argparse.ArgumentParser(description="Run NYPD data analysis")
    parser.add_argument("--input_dir", required=True, help="Path to the input data directory")
    parser.add_argument("--output_file", required=True, help="Path to the output CSV file")
    args = parser.parse_args()

    print(f"Loading data from: {args.input_dir}")

    paths = {
        'alcohol': os.path.join(args.input_dir, "alcohol.csv"),
        'area': os.path.join(args.input_dir, "area.csv"),
        'fires': os.path.join(args.input_dir, "fires.csv"),
        'population': os.path.join(args.input_dir, "population.csv"),
    }

    raw_data = {key: data_loader.load_csv(path) for key, path in paths.items()}
    cleaned_data = data_cleaner.clean_data(raw_data)

    print("\nAvailable columns in cleaned data:")
    for key, df in cleaned_data.items():
        print(f"{key.upper()}: {df.columns.tolist()}")

    
    analysis_results = analyzer.analyze_data(cleaned_data)
    analyze_hypotheses(analysis_results)

    reporter.save_report(analysis_results, args.output_file)

    print(f"\nAnalysis complete. Results saved to: {args.output_file}")
    print(analysis_results.head())
    print(f"Total rows: {analysis_results.shape[0]}, columns: {analysis_results.shape[1]}")

if __name__ == "__main__":
    main()
