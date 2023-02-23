"""
This script imports the data.
"""

import pandas as pd
import numpy as np

def read_data(file_path):
    """Reads in the data."""

    # Check if CSV, JSON, or XML file
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        df = pd.read_json(file_path)
    elif file_path.endswith('.xml'):
        df = pd.read_xml(file_path)
    else:
        raise ValueError('File type not supported.')
    return df