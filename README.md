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
├── analysis_lib/            # Core analysis package
│   ├── __main__.py          # CLI entry point (uses argparse)
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── analyzer.py
│   ├── hypotheses.py
│   └── reporter.py
├── my_data/                 # Sample input data (CSV)
├── notebooks/
│   └── analysis_demo.ipynb  # Jupyter usage example
├── profiling/
│   ├── profiler_output.txt  # Profiling results
│   └── profiling_explanation.md
├── tests/
│   └── ...                  # Unit tests
├── setup.py                 # pip installation script
├── README.md                # Documentation
└── requirements.txt         # Dependencies
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
notebooks/analysis_demo.ipynb
```

---

## Author

**Viktor Ilyk**  
3rd-year Computer Science student  
Spring 24/25 — Final Assignment  
