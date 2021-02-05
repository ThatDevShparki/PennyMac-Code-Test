import pandas as pd

def import_data(filename):
    """
    imports the given file to a Pandas DataFrame object
    removes any rows containing null values
    returns the Pandas DataFrame object
    """
    df = pd.read_csv(filename, 
                 sep = '\s+',
                 header = 1,
                 skiprows = None, 
                 usecols = [4,6],
                 names = ["F","A"],
                 engine = 'python')
    df = df.dropna()
    return df

def get_team_name(index):
    """
    isolates the team name from the column brought from the DataFrame's index
    returns the team name
    """
    team_name = index[1]
    return team_name

def goal_diff(row):
    """
    calculates the difference between Goals For and Goals Against in a row
    returns the absolute value of difference in goals
    """
    diff = abs(row['F'] - row['A'])
    return diff

def main():
    df = import_data("soccer.dat")
    df['Team'] = df.index
    df['Team'] = df['Team'].apply(get_team_name)
    df['Diff'] = df.apply (lambda row: goal_diff(row), axis=1)
    df = df.sort_values('Diff')
    team_name = df['Team'].iloc[0]
    print("team", team_name, "had the smallest difference in 'for' and 'against' goals")

if __name__ == "__main__":
    main()

