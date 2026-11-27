"""Small reusable helper functions."""


def get_numeric_columns(data):
    """Return the names of numeric columns in a DataFrame."""
    return list(data.select_dtypes(include="number").columns)
