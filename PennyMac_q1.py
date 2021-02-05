import pandas as pd

def import_data(filename):
    """
    imports the given file to a Pandas DataFrame object
    removes any rows containing null values
    returns the Pandas DataFrame object
    """
    df = pd.read_csv(filename, 
                 sep = '\s+',
                 header = 2,
                 skiprows = 1, 
                 usecols = [0,1,2])
    df = df.dropna()
    return df

def temperature_clean(temperature):
    """
    cleans any temperature values containing an asterisks
    returns a float of the cleaned temperature values
    """
    clean_temperature = temperature.replace('*','')
    float_temperature = float(clean_temperature)
    return float_temperature

def temperature_diff(row):
    """
    calculates the difference between max temperature and min temperature in a row
    returns the temperature difference
    """
    temperature_diff = temperature_clean(row['MxT']) - temperature_clean(row['MnT'])
    return temperature_diff

def main():
    df = import_data("w_data.dat")
    df['Diff'] = df.apply (lambda row: temperature_diff(row), axis=1)
    df = df.sort_values('Diff')
    day_num = df['Dy'].iloc[0]
    print("day", day_num, "had the smallest temperature spread")

if __name__ == "__main__":
    main()

