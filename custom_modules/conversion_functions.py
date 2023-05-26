import pandas as pd
import numpy as np
from typing import List

def convert_to_df(cars_data: List) -> pd.DataFrame:
    '''
    Converts a list of cars to a pandas Data Frame

    Parameters:
    * cars_data 

    Returns:
    * cars_df_subset
    
    '''
    # convert to pandas DataFrame
    cars_df = pd.DataFrame(cars_data)

    # list with selected columns
    selected_columns = ['merk', 'handelsbenaming', 'eerste_kleur', 'catalogusprijs']

    # create a subset of the dataset
    available_columns = cars_df.columns

    for column in selected_columns:
        if column not in available_columns:
            cars_df[column] = np.nan

    cars_df_subset = cars_df[selected_columns]

    return cars_df_subset