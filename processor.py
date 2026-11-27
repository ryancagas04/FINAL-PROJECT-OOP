"""Base class shared by Cleanalyze processing tools."""
from .dataset import Dataset


class DataProcessor:
    """Base class that owns a Dataset and defines a common processing interface."""

    def __init__(self, data):
        """Accept a Dataset or raw data and store it as a Dataset."""
        self._dataset = data if isinstance(data, Dataset) else Dataset(data)

    @property
    def dataset(self):
        """Return the Dataset managed by this processor."""
        return self._dataset

    def process(self):
        """Return the current dataset; subclasses can override this method."""
        return self._dataset.data

    def get_data(self):
        """Return a safe copy of the current data."""
        return self._dataset.data
