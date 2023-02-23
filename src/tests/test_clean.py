import unittest
import pandas as pd
from src.clean import (
    read_data,
    replace_missing_values_with_new_value,
    replace_missing_values_with_mean,
    drop_column_above_ratio_of_missing_values,
)


class TestCSVCleaning(unittest.TestCase):
    def test_load_and_clean(self):
        """Tests the load and clean function."""

        # Load the CSV file
        super().__init__()
        df = read_data("test.csv")
        # Check if the data is loaded
        self.assertEqual(df.shape, (10, 3))

        # Clean the data in second column
        df["Interest"] = replace_missing_values_with_new_value(df["Interest"], "NA")

        # Clean data in third column
        df["Average"] = replace_missing_values_with_mean(df["Average"])

        # Clean data in fourth column
        df = drop_column_above_ratio_of_missing_values(df, 0.5)

        # Check if the data is cleaned
        self.assertEqual(df.isnull().sum().sum(), 0)


if __name__ == "__main__":
    unittest.main()
