import pandas as pd

def main():
    # load in the file movie selector/old.xlsx
    old = pd.read_csv("old.csv")
    old = old.sort_values(by='title')
    old.to_csv("old.csv", index=False)
    letterboxd = pd.read_csv("letterboxd.csv")

    # clean up datasets for merge operation
    letterboxd['Name'] = letterboxd['Name'].str.lower()
    # 'how' parameter defines the type of join (inner, left, right, outer)
    merged_df = pd.merge(old, letterboxd, left_on='title', right_on='Name', how='outer')
    merged_df = merged_df[['title', 'Name', 'provider', 'runtime']].sort_values(by='title')

    # Optional: Save the merged DataFrame to a new CSV file
    merged_df.to_csv("watchlist.csv", index=False)


if __name__ == "__main__":
    main()