import pandas as pd

def clean_scraped_data(raw_data):
    df = pd.DataFrame(raw_data)
    df.drop_duplicates(inplace=True)
    df.fillna("", inplace=True)
    return df
