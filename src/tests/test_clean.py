import unittest

from src.clean import (
    drop_column_above_ratio_of_missing_values,
    read_data,
    replace_missing_values_with_mean,
    replace_missing_values_with_new_value,
)


class TestCSVCleaning(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Load dataframe from CSV file."""
        cls.df = read_data("src/tests/test.csv")

    def test_read_data(self) -> None:
        """Tests the read data function."""
        self.assertEqual(self.df.shape, (10, 4))

    def test_replace_missing_values_with_new_value(self) -> None:
        """Tests the replace missing values with new value function."""
        df = self.df.copy()
        df["Interest"] = replace_missing_values_with_new_value(df["Interest"], "NA")
        self.assertEqual(df["Interest"].isnull().sum(), 0)

    def test_replace_missing_values_with_mean(self) -> None:
        """Tests the replace missing values with mean function."""
        df = self.df.copy()
        df["Average"] = replace_missing_values_with_mean(df["Average"])
        self.assertEqual(df["Average"].isnull().sum(), 0)

    def test_drop_column_above_ratio_of_missing_values(self) -> None:
        """Tests the drop column above ratio of missing values function."""
        df = self.df.copy()
        drop_column_above_ratio_of_missing_values(df, "Age", 0.80)
        self.assertEqual(df.shape, (10, 3))



if __name__ == "__main__":
    unittest.main()
