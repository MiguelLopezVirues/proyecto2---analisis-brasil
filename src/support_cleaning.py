import numpy as np
import pandas as pd
from tqdm import tqdm
tqdm.pandas() 

def normalize(s):
    """
    Function to normalize by:
    - Passing accented letters to accent-less.
    - Replacing spaces.
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
        ("ô","o"),
        ("ç","c"),
        ("ã","a"),

    )
    for a, b in replacements:
        s = s.lower().replace(a, b).replace(" ","_")
    return s

def apply_fill(df, direction="both"):

    # take just the first two columns to ensure proper output.
    df[["column1","column2"]] = df.iloc[:,[0,1]].copy()

    # create equivalences dict
    equivalences = df[["column1","column2"]].value_counts().index.to_list()
    equivalences_dict = {codigo: nome for codigo, nome  in equivalences}
    reversed_equivalences_dict = {column2: column1 for column1, column2 in equivalences_dict.items()}

    # create filters to correct only rows where there are NaNs
    column1_null = df["column1"].isna()
    column2_null = df["column2"].isna()

    if direction == "both":
        df.loc[column1_null & column2_null] = df.loc[column1_null & column2_null].progress_apply(
            lambda row: fill_value_bidirectional(row['column1'], row['column2'], equivalences_dict, reversed_equivalences_dict),
            axis=1,
            result_type='expand'
        )

    elif direction == "right":
        df.loc[column2_null] = df.loc[column2_null].progress_apply(
            lambda row: fill_value_unidirectional(row['column1'], row['column2'], equivalences_dict, reversed_equivalences_dict, direction="right"),
            axis=1,
            result_type='expand'
        )
        
    else:
        df.loc[column1_null] = df.loc[column1_null].progress_apply(
            lambda row: fill_value_unidirectional(row['column1'], row['column2'], equivalences_dict, reversed_equivalences_dict, direction="left"),
            axis=1,
            result_type='expand'
        )

    return df

# simplify
def fill_value_bidirectional(colum_value1, colum_value2, equivalence_dict, reversed_equivalences_dict):

    colum_value2 = equivalence_dict.get(colum_value1, np.nan)
    colum_value1 = reversed_equivalences_dict.get(colum_value2, np.nan)
    
    return colum_value1, colum_value2

def fill_value_unidirectional(colum_value1, colum_value2, equivalence_dict, reversed_equivalences_dict, direction="left"):

    if direction == "right":
        colum_value2 = equivalence_dict.get(colum_value1, np.nan)
    else:
        colum_value1 = reversed_equivalences_dict.get(colum_value2, np.nan)
    
    return colum_value1, colum_value2