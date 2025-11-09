import pandas as pd

def quick_look(df = pd.read_json('data/contacts.json')):
    info = f"{df.head()} \n\n{df.shape()} \n\n {df.info()}"
    return info

def name_alphabetic(df = pd.read_json('data/contacts.json')):
    sorted_df = df.sort_values(by='name',  key=lambda col: col.str.lower())
    return sorted_df.to_dict(orient='records')

def group_by_company(df = pd.read_json('data/contacts.json')):
    grouped = df.groupby('company').apply(lambda x: x.to_dict(orient='records')).to_dict()
    return grouped