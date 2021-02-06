"""
program to determine which day had the smallest temperature difference
data is initially imported to Pandas DataFrame
columns used to preform the difference calculation are cleaned
difference between max and min temperatures is calculated and stored in new column
data is sorted by that new 'difference' column
the day number of the top row is selected from the sorted DataFrame
"""

import pandas as pd
import PennyMac_fucntions as pmf


def temperature_clean(temperature):
    """
    cleans any temperature values containing an asterisks
    returns a float of the cleaned temperature values
    """
    clean_temperature = temperature.replace('*', '')
    int_temperature = int(clean_temperature)
    return int_temperature


def main():
    df = pmf.import_data("w_data.dat", 2, 1, [0, 1, 2])
    df = df[df['Dy'] != 'mo']
    df['MxT'] = df.apply(lambda row: temperature_clean(row['MxT']), axis=1)
    df['MnT'] = df.apply(lambda row: temperature_clean(row['MnT']), axis=1)
    df['Diff'] = df.apply(lambda row: pmf.difference(row, 'MxT', 'MnT'), axis=1)
    df = df.sort_values('Diff')
    day_num = df['Dy'].iloc[0]
    print(f"day {day_num} had the smallest temperature spread")  # 14


if __name__ == "__main__":
    main()
