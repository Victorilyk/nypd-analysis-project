# NYPD Analysis Project

Final assignment for the “Data in Python” course (Spring 2024/2025).

This Python package performs data analysis on Polish public datasets related to fire incidents (PSP), alcohol-selling licenses, population, and local administrative areas (JST).  
It computes correlations, cleans and validates data, and exports a statistical report.

---

## Installation

Clone the repository and install the package locally:

```bash
git clone https://github.com/Victorilyk/nypd-analysis-project.git
cd nypd-analysis-project
pip install .
```

> Requires: Python 3.9+ and `pandas`

---

## Usage

Run the project using the CLI module:

```bash
python -m analysis_lib --input_dir my_data/ --output_file output.csv
```

- `--input_dir`: Folder containing the following files:
  - `alcohol.csv`
  - `area.csv`
  - `fires.csv`
  - `population.csv`
- `--output_file`: CSV file where analysis results will be saved

---

## Project Structure

```
nypd-analysis-project/
├── analysis_lib/                      #  Main Python package with all business logic
│   ├── __main__.py                    #  Entry point for the command-line interface (uses argparse)
│   ├── data_loader.py                 #  Module for loading CSV data from a specified folder
│   ├── data_cleaner.py                #  Module to clean and validate the data (missing values, type casting)
│   ├── analyzer.py                    #  Module for statistical analysis and correlation computations
│   ├── hypotheses.py                  #  Optional: Custom hypotheses analysis (e.g., population density vs fire rate)
│   └── reporter.py                    #  Handles exporting results to CSV/JSON and logs dropped data
│
├── my_data/                           #  Folder with input data (CSV files): alcohol.csv, area.csv, fires.csv, population.csv
│   ├── alcohol.csv                    #  Number of alcohol-selling places by region
│   ├── area.csv                       #  Area size per region
│   ├── fires.csv                      #  Number of fire events per region
│   └── population.csv                 #  Population count per region
│
├── notebooks/                         #  Jupyter notebooks for demonstrating usage of the package
│   └── analysis_demo.ipynb           #  Example notebook with step-by-step code: loading, cleaning, analysis
│
├── profiling/                         #  Folder with performance profiling results and explanation
│   ├── profiler_output.txt           #  Output from a profiling run showing execution time per function
│   └── profiling_explanation.md      #  Text file explaining potential bottlenecks based on profiler results
│
├── tests/                             #  Folder with unit tests for each module
│   ├── test_loader.py                #  Tests for data loading
│   ├── test_cleaner.py               #  Tests for data cleaning
│   ├── test_analyzer.py              #  Tests for correlation and statistics
│   └── __init__.py                   # (optional) Marks this as a test package
│
├── setup.py                           #  Installation script for pip (defines name, version, entry point etc.)
├── README.md                          #  Main documentation file with description, usage, structure, and instructions
├── requirements.txt                   #  List of dependencies (e.g., pandas, numpy, pytest)
└── .gitignore                         #  Optional: Excludes virtual environments, cache, and output files from git

```

---

## Hypotheses Analyzed

1. 📈 **Population vs Fire Events**
2. 🍻 **Population vs Alcohol-Selling Points**
3. 🔥 **Alcohol-Selling Points vs Fire Events**
4. 💡 **Population Density vs Fire Rate** (custom hypothesis)

Each hypothesis is tested using Pearson correlation, with results printed and saved to CSV.

---

## Running Tests

Install testing tools and run:

```bash
pip install pytest
pytest tests/
```

---

## Profiling

Profiling results are available in:

```
profiling/profiler_output.txt
```

They include execution time per function. Bottlenecks are discussed in `profiling_explanation.md`.

To re-run profiling:

```bash
python profiling/profile_analysis.py
```

---

## Jupyter Example

A usage demo is provided in:

```
jupyter notebook

```

---

## Author

**Viktor Ilyk**  
3rd-year Computer Science student  
Spring 24/25 — Final Assignment  
