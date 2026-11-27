"""Dataset container used by the Cleanalyze processing classes."""
import pandas as pd


class Dataset:
    """Store a pandas DataFrame and provide controlled access to its data."""

    def __init__(self, data):
        """Create a Dataset from a DataFrame or data accepted by pandas."""
        if isinstance(data, pd.DataFrame):
            self.__data = data.copy()
        else:
            self.__data = pd.DataFrame(data)

    @property
    def data(self):
        """Return a copy of the stored DataFrame."""
        return self.__data.copy()

    @data.setter
    def data(self, new_data):
        """Replace the stored data after checking its type."""
        if not isinstance(new_data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame")
        self.__data = new_data.copy()

    def __len__(self):
        """Return the number of rows."""
        return len(self.__data)

    def __repr__(self):
        """Return a useful description of the dataset."""
        return f"Dataset(rows={len(self.__data)}, columns={len(self.__data.columns)})"

    def __eq__(self, other):
        """Compare two Dataset objects by their contents."""
        return isinstance(other, Dataset) and self.__data.equals(other.__data)
