import pandas as pd
import itertools
import csv

# Headings for the final generated data
HEADERS = [***]

def init():
    pass


def generate_rows(source):
    # Sorry, but the generate function content is a private property.
    
    return rows


def run(mini_batch: pd.DataFrame):
    all_rows = []
    for _, row in mini_batch.iterrows():
        data = generate_rows(row.tolist())
        all_rows.extend(data)
    return pd.DataFrame(all_rows, columns=HEADERS)
