import pandas as pd


def scale_data(train, validate, test):
    '''
    Scale the text using a TFIDF scaler
    '''
    cols_to_scale = []

    # Create a list of new scaled column names
    scaled_cols = [f'scaled_{col}' for col in cols_to_scale]


    def tf_idf(train, validate, test):
        '''
        
        '''
        # Create the Scaler Object
        scaler = '[TFIDFSCALER]'

        # Fit the scaler to the training set and transform the train, validate, and test sets.
        train[scaled_cols] = scaler.fit_transform(train[cols_to_scale])
        validate[scaled_cols] = scaler.transform(validate[cols_to_scale])
        test[scaled_cols] = scaler.transform(test[cols_to_scale])

        return train, validate, test


    # Scale and arrange the columns in the train, validate, and test sets.
    train, validate, test = tf_idf(train, validate, test)

    return train, validate, test