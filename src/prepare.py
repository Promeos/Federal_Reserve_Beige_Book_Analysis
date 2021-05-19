import pandas as pd
import numpy as np

from pandas.api.types import CategoricalDtype


def prep_beige_data(dataset):
    '''
    Returns 

    Parameters
    ----------
    None 
    
    Returns
    -------
    '''
    dataset = format_column_names(dataset)

    return dataset


def format_column_names(dataset):
    '''
    Formats all column names to be lowecase and replaces column names
    with descriptive names.

    Parameters
    ----------
    dataset
    
    Returns
    -------
    dataset
    '''
    # Lowercase the column names
    dataset.columns = [column.lower() for column in dataset.columns]

    # Rename columns with more descriptive names
    dataset.rename(columns={'[name]':'[new name]'},
                   inplace=True)

    return dataset




