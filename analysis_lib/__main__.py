import argparse
import os
from analysis_lib import data_loader, data_cleaner, analyzer, reporter

def main():
    parser = argparse.ArgumentParser(description="Run NYPD data analysis")
    parser.add_argument("--input_dir", required=True, help="Path to the input data directory")
    parser.add_argument("--output_file", required=True, help="Path to the output CSV file")
    args = parser.parse_args()

    print(f"Loading data from: {args.input_dir}")

    # Construct file paths
    paths = {
        'alcohol': os.path.join(args.input_dir, "alcohol.csv"),
        'area': os.path.join(args.input_dir, "area.csv"),
        'fires': os.path.join(args.input_dir, "fires.csv"),
        'population': os.path.join(args.input_dir, "population.csv"),
    }

    # Load all files using data_loader
    raw_data = {key: data_loader.load_csv(path) for key, path in paths.items()}

    # Clean data
    cleaned_data = data_cleaner.clean_data(raw_data)

    # Analyze cleaned data
    analysis_results = analyzer.analyze_data(cleaned_data)

    # Save report
    reporter.save_report(analysis_results, args.output_file)

    print(f"Analysis complete. Results saved to: {args.output_file}")
    print(analysis_results.head())
    print(f"Total rows: {analysis_results.shape[0]}, columns: {analysis_results.shape[1]}")

if __name__ == "__main__":
    main()
