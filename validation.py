"""Dataset validation helpers."""
import pandas as pd


def validate_dataset(data):
    """Check whether data is a non-empty pandas DataFrame; return a report."""
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame")
    if data.empty:
        return {"valid": False, "rows": 0, "columns": len(data.columns),
                "message": "The dataset has no rows."}
    return {"valid": True, "rows": len(data), "columns": len(data.columns),
            "missing_values": int(data.isna().sum().sum()),
            "duplicate_rows": int(data.duplicated().sum()),
            "message": "Dataset loaded successfully."}
