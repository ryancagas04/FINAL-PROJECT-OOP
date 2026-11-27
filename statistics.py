"""Basic statistical analysis operations."""
from .processor import DataProcessor


class DataAnalyzer(DataProcessor):
    """Calculate descriptive statistics for numeric columns."""

    def process(self):
        """Override process to return a descriptive statistical summary."""
        return self.get_summary()

    def get_summary(self):
        """Return count, mean, standard deviation, minimum, and maximum."""
        return self._dataset.data.describe()

    def get_mean(self, column):
        """Return the mean of a selected numeric column."""
        return float(self._dataset.data[column].mean())

    def get_median(self, column):
        """Return the median of a selected numeric column."""
        return float(self._dataset.data[column].median())

    def get_standard_deviation(self, column):
        """Return the sample standard deviation of a selected numeric column."""
        return float(self._dataset.data[column].std())
