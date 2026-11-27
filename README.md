# Cleanalyze

**A beginner-friendly Python library for data cleaning and basic statistical analysis.**

Cleanalyze is a small educational project that demonstrates how Object-Oriented Programming (OOP) can organize common data science tasks. It uses pandas for tabular data and matplotlib for charts.

## Features
- Replace missing values or remove rows with missing values
- Remove duplicate records
- Generate descriptive statistics
- Calculate mean, median, and standard deviation
- Validate a dataset
- Create histograms and bar charts

## Installation

For development, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Install the package locally from the project root:

```bash
python -m pip install .
```

## Quick example

```python
import pandas as pd
from cleanalyze import DataCleaner, DataAnalyzer

data = pd.DataFrame({"score": [80, None, 90, 90]})

cleaner = DataCleaner(data)
cleaned_data = cleaner.process()

analyzer = DataAnalyzer(cleaned_data)
print(analyzer.get_summary())
print(analyzer.get_mean("score"))
```

Run the demonstration:

```bash
python demo.py
```

Run tests:

```bash
python -m unittest discover -s tests
```

## OOP concepts demonstrated
- **Classes:** `Dataset`, `DataProcessor`, `DataCleaner`, `DataAnalyzer`, and `DataVisualizer`
- **Encapsulation:** `Dataset` stores its DataFrame in a private attribute and exposes a property that returns a copy.
- **Inheritance:** the cleaning, analysis, and visualization classes inherit from `DataProcessor`.
- **Polymorphism:** each child class overrides `process()` for its own task.
- **Dunder methods:** `Dataset` implements `__len__`, `__repr__`, and `__eq__`.
- **Composition:** each processor owns a `Dataset` object.

## Project structure

```text
cleanalyze/
├── cleanalyze/
│   ├── __init__.py
│   ├── dataset.py
│   ├── processor.py
│   ├── cleaning.py
│   ├── statistics.py
│   ├── visualization.py
│   ├── validation.py
│   └── utils.py
├── tests/
├── demo.py
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

## Project status
This is an educational project version (0.1.0). Test the package locally before publishing. PyPI publication requires a project account, package-name availability check, and a successful TestPyPI upload first.

## Contributors

- John Vince J. Ambrosio
- James Ryan Cagas
- Reyben W. Ortega
- Kent Isaac B. Quilicot

