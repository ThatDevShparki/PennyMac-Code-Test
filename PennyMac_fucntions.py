"""
functions that are usable in both Code Test solutions
"""

import pandas as pd


def import_data(filename, head, skip, use, name=None, eng=None):
    """
    imports the given file to a Pandas DataFrame object
    removes any rows containing null values
    returns the Pandas DataFrame object
    """
    df = pd.read_csv(filename,
                 sep = '\s+',
                 header = head,
                 skiprows = skip,
                 usecols = use,
                 names = name,
                 engine = eng)
    df = df.dropna()
    return df


def difference(row, col1, col2):
    """
    calculates the difference between 2 specified columns within a row in a Pandas DataFrame
    returns the difference value
    """
    diff = row[col1] - row[col2]
    return diff
