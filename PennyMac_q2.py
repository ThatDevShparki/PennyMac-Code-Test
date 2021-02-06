"""
program to determine which team had the smallest difference in 'For' and 'Against' goals
data is initially imported to Pandas DataFrame
team name column is derived from the DataFrame's index
absolute value of difference in 'For' and 'Against' goals is calculated and stored in new column
data is sorted by that new 'difference' column
the team name of the top row is selected from the sorted DataFrame
"""

import pandas as pd
import PennyMac_fucntions as pmf


def main():
    df = pmf.import_data("soccer.dat", 1, None, [4, 6], ["F", "A"], 'python')
    df[['Row', 'Team']] = pd.DataFrame(df.index.tolist(), index=df.index)
    df['Diff'] = df.apply(lambda row: abs(pmf.difference(row, 'F', 'A')), axis=1)
    df = df.sort_values('Diff')
    team_name = df['Team'].iloc[0]
    print(f"team {team_name} had the smallest difference in 'for' and 'against' goals")  # Aston_Villa


if __name__ == "__main__":
    main()
