import argparse
import os
from analysis_lib import data_loader, data_cleaner, analyzer, reporter

def main():
    parser = argparse.ArgumentParser(description="Run NYPD data analysis")
    parser.add_argument("--input_dir", required=True, help="Path to the input data directory")
    parser.add_argument("--output_file", required=True, help="Path to the output CSV file")

    args = parser.parse_args()

    print(f"📥 Loading data from: {args.input_dir}")

    # Load individual CSV files
    alcohol_path = os.path.join(args.input_dir, "alcohol.csv")
    area_path = os.path.join(args.input_dir, "area.csv")
    fires_path = os.path.join(args.input_dir, "fires.csv")
    population_path = os.path.join(args.input_dir, "population.csv")

    alcohol_df = data_loader.load_csv(alcohol_path)
    area_df = data_loader.load_csv(area_path)
    fires_df = data_loader.load_csv(fires_path)
    population_df = data_loader.load_csv(population_path)

    # Clean data using single function
    data_dict = {
        'alcohol': alcohol_df,
        'area': area_df,
        'fires': fires_df,
        'population': population_df
    }

    cleaned_data = data_cleaner.clean_data(data_dict)

    alcohol_df = cleaned_data['alcohol']
    area_df = cleaned_data['area']
    fires_df = cleaned_data['fires']
    population_df = cleaned_data['population']

    # Analyze data
    analysis_results = analyzer.analyze_data(cleaned_data)
    # Save report
    reporter.save_report(analysis_results, args.output_file)

    print(f"Analysis complete. Results saved to: {args.output_file}")
    print(analysis_results.head())
    print(analysis_results.shape)
