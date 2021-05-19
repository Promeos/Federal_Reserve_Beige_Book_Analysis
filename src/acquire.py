# Acquire File
import pandas as pd
import numpy as np
import os


###################### Acquire Beige Book Data ########################
def get_beige_data():
    '''
    Acquires the Beige Book dataset from `beige_book.csv`.
    Returns a Pandas DataFrame.

    Parameters
    ----------
    None 
    
    Returns
    -------
    df : pandas.core.frame.DataFrame
       Beige Book dataset. 
    '''

    try:
        return pd.read_csv('./data/beige_book.csv')
    except:
        raise FileNotFoundError("You're missing the file named 'beige_book.csv'. You can acquire the data here: [link]")