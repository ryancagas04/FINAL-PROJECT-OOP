"""Data cleaning operations."""
from .processor import DataProcessor


class DataCleaner(DataProcessor):
    """Clean missing values and duplicate rows in a dataset."""

    def process(self):
        """Override the common process method with a basic cleaning workflow."""
        self.remove_duplicates()
        self.fill_missing()
        return self.get_data()

    def fill_missing(self, value=0):
        """Replace missing values with the supplied value and return the result."""
        cleaned = self._dataset.data.fillna(value)
        self._dataset.data = cleaned
        return self.get_data()

    def remove_duplicates(self):
        """Remove duplicate rows and return the cleaned data."""
        cleaned = self._dataset.data.drop_duplicates()
        self._dataset.data = cleaned
        return self.get_data()

    def drop_missing(self):
        """Remove rows containing at least one missing value."""
        self._dataset.data = self._dataset.data.dropna()
        return self.get_data()
