import numpy as np
import pandas as pd
from tqdm import tqdm
import Levenshtein as lev
import re

tqdm.pandas() 

def normalize(s):
    """
    Function to normalize by:
    - Passing accented letters to accent-less.
    - Transforming to lowercase.

    Args:
        s (str): string to normalize for accents

    Returns:
        str: normalized string
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ô", "o"),
        ("ç", "c"),
        ("ã", "a"),
        ("õ", "o"),
        ("â", "a"),
        ("ê", "e"),
        ("î", "i"),
        ("ù", "u"),
        ("ä", "a"),
        ("ë", "e"),
        ("ï", "i"),
        ("ö", "o"),
        ("ü", "u"),
        ("ÿ", "y"),
        ("à", "a"),
        ("è", "e"),
        ("ì", "i"),
        ("ò", "o"),
        ("ù", "u"),
        ("/","_"),
        ("ñ ",""),
        ("-","_"),
        (" ","_"),
        (".","_"),
        ("(","_"),
        (")","_"),
        (",","_"),
    )
    for a, b in replacements:
        s = s.lower().replace(a, b)
    
    s = re.sub(r'_+', '_', s)
    return s


def fill_categories(df_original):
    df = df_original.iloc[:,[0,1]].copy()
    column1, column2 = df.columns.to_list()
    column1_column2_equivalences = df.value_counts().reset_index()
    print(f"Full unique combinations: {column1_column2_equivalences.shape[0]}")
    column1_column2_equivalences_unique_column2 = column1_column2_equivalences.drop_duplicates(subset=column2,keep=False)
    print(f"Unique combinations of one {column2} to one {column1}: {column1_column2_equivalences_unique_column2.shape[0]}")

    column1_column2_equivalences_unique_column1 = column1_column2_equivalences_unique_column2[[column1, column2]].values

    equivalences_dict = {column2: column1 for column1, column2  in column1_column2_equivalences_unique_column1}

    df[column1] = (df[column1]
                    .fillna(df[column2]
                    .map(equivalences_dict)))
    
    return df

def fill_categories_forward_backward_massive(df_original):
    # forward
    for column_idx in range(len(df_original.columns) - 1):
        df_original.iloc[:,[column_idx,column_idx + 1]] = fill_categories_forward_backward(df_original.iloc[:,[column_idx,column_idx + 1]])
    
    # backward
    df_reversed = df_original[df_original.columns[::-1]]
    for column_idx in range(len(df_original.columns) - 1):
        df_reversed.iloc[:,[column_idx,column_idx + 1]] = fill_categories_forward_backward(df_reversed.iloc[:,[column_idx,column_idx + 1]])

    df_original = df_reversed[df_reversed.columns[::-1]]
    
    return df_original

def fill_categories_forward_backward(df_original):
    df = df_original.iloc[:,[0,1]].copy()
    df = fill_categories(df)
    df_reversed = df[df.columns[::-1]]
    df_reversed = fill_categories(df_reversed)
    df = df_reversed[df_reversed.columns[::-1]]
    return df


def find_similar_values(column, distance=2):
    similar_pairs = []
    values = column.dropna().unique()  
    
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if lev.distance(values[i], values[j]) <= distance:
                similar_pairs.append((values[i], values[j]))
    return similar_pairs