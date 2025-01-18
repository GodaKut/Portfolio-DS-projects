import pandas as pd


def handle_duplicates_method(df, col=None):
    if col == None:
        if df.duplicated().any():
            duplicated_observations = df.duplicated().sum()
            df.drop_duplicates(keep="first", inplace=True)
            return f"Found and deleted {duplicated_observations} duplicate(s)."

        else:
            return "No duplicates found."
    else:
        if df.duplicated(subset=col).any():
            df.drop_duplicates(keep="first", inplace=True)
            duplicated_observations = df.duplicated().sum()
        else:
            return "No duplicates found."
