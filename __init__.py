"""Cleanalyze: beginner-friendly data cleaning and analysis tools."""
from .dataset import Dataset
from .processor import DataProcessor
from .cleaning import DataCleaner
from .statistics import DataAnalyzer
from .visualization import DataVisualizer
from .validation import validate_dataset

__version__ = "0.1.0"

__all__ = [
    "Dataset", "DataProcessor", "DataCleaner",
    "DataAnalyzer", "DataVisualizer", "validate_dataset"
]
