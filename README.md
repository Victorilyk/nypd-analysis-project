# NYPD Analysis Project

Final assignment for the “Data in Python” course (Spring 2024/2025).

This Python package performs data analysis on public datasets related to fires, alcohol licenses, population, and administrative areas (JST). It calculates correlations, checks data quality, and generates a clean report.

---

## Installation

```bash
pip install .
```

---

## Usage

You can run the analysis from the command line using:

```bash
run-analysis --input_dir my_data --output_file my_data/final_output.csv
```

- `--input_dir` – folder with input CSV files (`alcohol.csv`, `area.csv`, `fires.csv`, `population.csv`)
- `--output_file` – file where the result of analysis will be saved

---

## Project Structure

```
nypd_analysis_project/
├── analysis_lib/            # Core library
├── my_data/                 # Input CSV files
├── notebooks/               # Jupyter notebook demo
├── profiling/               # Profiling results
├── scripts/                 # Optional run scripts
├── tests/                   # Unit tests
├── README.md                # Documentation
├── setup.py                 # Installation script
└── requirements.txt         # Dependencies
```

---

## Hypotheses analyzed

1. 📈 Does a higher population in an area lead to more fire events?
2. 🍻 Is there a link between population size and the number of alcohol licenses?
3. 🔥 Are alcohol-selling companies associated with fire frequency?
4. 💡 Own hypothesis: Is there a correlation between population density and fire risk?

Each correlation is calculated using grouped and cleaned data, and exported to a CSV file.

---

## Running Tests

```bash
pip install pytest
pytest tests/
```

---

## Profiling

Profiling results can be found in:
```
profiling/profiler_output.txt
```

This includes detailed timing information about each function in the analysis pipeline. Bottlenecks (if any) are highlighted in the final exam discussion.

---

## Author

**Viktor Ilyk**  
3rd-year Computer Science student  
Spring 24/25 – Final Assignment
