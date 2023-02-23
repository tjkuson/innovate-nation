"""
This script cleans the data.
"""
import os

import numpy as np
import pandas as pd


def read_data(file_path: str) -> pd.DataFrame:
    """Reads in the data."""

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found.")

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


def replace_missing_values_with_new_value(df, new_value=0):
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


def drop_row(df):
    """Drops rows with missing values."""
    return df.dropna(axis=0)


def consists_of_numeric_values(df) -> bool:
    """Checks if the dataframe consists of numeric values."""
    # FIXME: This is not working
    return df.applymap(np.isreal).all().all()


def clean(df):
    """Cleans the data."""

    # Loop through columns and ask use what they want to do
    for column in df.columns:
        while True:
            print(f"Column: {column}")
            print("1. Replace missing values with new value")
            print("2. Replace missing values with mean")
            print("3. Replace missing values with median")
            print("4. Replace missing values with mode")
            print("5. Drop column above ratio of missing values")
            print("6. Drop rows with missing values")
            print("7. Do nothing")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_value = input("Enter new value: ")
                try:
                    new_value = int(new_value)
                except ValueError:
                    pass
                try:
                    new_value = float(new_value)
                except ValueError:
                    pass
                df[column] = replace_missing_values_with_new_value(
                    df[column], new_value
                )
                break
            elif choice == "2":
                if consists_of_numeric_values(df[column]):
                    df[column] = replace_missing_values_with_mean(df[column])
                    break
                else:
                    print("Column is not numeric. Please try again.")
                    continue
            elif choice == "3":
                if consists_of_numeric_values(df[column]):
                    df[column] = replace_missing_values_with_median(df[column])
                    break
                else:
                    print("Column is not numeric. Please try again.")
                    continue
            elif choice == "4":
                df[column] = replace_missing_values_with_mode(df[column])
                break
            elif choice == "5":
                ratio = input("Enter ratio of missing values to values: ")
                try:
                    ratio = float(ratio)
                    if ratio > 1 or ratio < 0:
                        raise ValueError
                except ValueError:
                    print("Invalid ratio. Please try again.")
                    continue
                df = drop_column_above_ratio_of_missing_values(df, ratio)
                break
            elif choice == "6":
                df = drop_row(df)
                break
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    # Get file
    while True:
        file_path = input("Enter the file path: ")
        try:
            df = read_data(file_path)
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
        except ValueError:
            print("File type not supported. Please try again.")

    # Clean the data
    clean(df)

    # Save the data
    while True:
        # Get export file format
        while True:
            print("1. CSV")
            print("2. JSON")
            print("3. XML")
            choice = input("Enter your choice: ")
            if choice == "1":
                file_format = "csv"
                break
            elif choice == "2":
                file_format = "json"
                break
            elif choice == "3":
                file_format = "xml"
                break
            else:
                print("Invalid choice. Please try again.")
        # Get export file name
        file_name = input("Enter the file name: ")
        if not file_name.endswith(f".{file_format}"):
            file_name += f".{file_format}"
        # Check if file exists
        if os.path.exists(file_name):
            print("File already exists. Please try again.")
            continue
        # Save the data
        if file_format == "csv":
            df.to_csv(file_name, index=False)
        elif file_format == "json":
            df.to_json(file_name, orient="records")
        elif file_format == "xml":
            df.to_xml(file_name, index=False)
        break


if __name__ == "__main__":
    main()
