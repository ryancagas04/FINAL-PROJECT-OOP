"""Unit tests for the main Cleanalyze features."""
import unittest
import pandas as pd
from cleanalyze import Dataset, DataCleaner, DataAnalyzer, validate_dataset


class TestCleanalyze(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "name": ["A", "B", "B"],
            "score": [10, None, None]
        })

    def test_dataset_length_and_repr(self):
        dataset = Dataset(self.data)
        self.assertEqual(len(dataset), 3)
        self.assertIn("Dataset", repr(dataset))

    def test_cleaning_removes_duplicates_and_fills_missing(self):
        result = DataCleaner(self.data).process()
        self.assertEqual(len(result), 2)
        self.assertFalse(result.isna().any().any())

    def test_analyzer_mean(self):
        analyzer = DataAnalyzer(pd.DataFrame({"score": [10, 20, 30]}))
        self.assertEqual(analyzer.get_mean("score"), 20.0)

    def test_validation(self):
        report = validate_dataset(self.data)
        self.assertTrue(report["valid"])
        self.assertEqual(report["rows"], 3)


if __name__ == "__main__":
    unittest.main()
