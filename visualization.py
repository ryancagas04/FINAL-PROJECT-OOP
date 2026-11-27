"""Basic plotting functions."""
from .processor import DataProcessor


class DataVisualizer(DataProcessor):
    """Create simple charts from a dataset."""

    def process(self):
        """Override process to return a short description of available columns."""
        return list(self._dataset.data.columns)

    def create_histogram(self, column, bins=10):
        """Create and return a histogram figure for a numeric column."""
        import matplotlib.pyplot as plt
        ax = self._dataset.data[column].plot(kind="hist", bins=bins, title=f"Histogram of {column}")
        ax.set_xlabel(column)
        return ax.get_figure()

    def create_bar_chart(self, column):
        """Create and return a bar chart of category counts."""
        import matplotlib.pyplot as plt
        counts = self._dataset.data[column].value_counts()
        ax = counts.plot(kind="bar", title=f"Counts for {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Count")
        return ax.get_figure()
