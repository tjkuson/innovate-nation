"""
This script cleans the data.
"""

import pandas as pd
import numpy as np


def read_data(file_path):
    """Reads in the data."""

    # Check if CSV, JSON, or XML file
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        df = pd.read_json(file_path)
    elif file_path.endswith(".xml"):
        df = pd.read_xml(file_path)
    else:
        raise ValueError("File type not supported.")
    return df


def get_missing_values(df):
    """Returns the position of missing values."""
    return df.isnull()


def repalce_missing_values_with_new_value(df, new_value=0):
    """Replaces missing values with new value. Default is 0."""
    return df.fillna(new_value)


def replace_missing_values_with_mean(df):
    """Replaces missing values with mean."""
    return df.fillna(df.mean())


def replace_missing_values_with_median(df):
    """Replaces missing values with median."""
    return df.fillna(df.median())


def replace_missing_values_with_mode(df):
    """Replaces missing values with mode."""
    return df.fillna(df.mode())


def drop_column_above_ratio_of_missing_values(df, ratio=0.5):
    """Drops columns with ratio of missing values above threshold."""
    return df.dropna(axis=1, thresh=ratio * len(df))


def drop_row_above_ratio_of_missing_values(df, ratio=0.5):
    """Drops rows with ratio of missing values above threshold."""
    return df.dropna(axis=0, thresh=ratio * len(df.columns))
