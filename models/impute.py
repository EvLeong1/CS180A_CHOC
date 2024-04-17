import pandas as pd
import numpy as np

df = pd.read_excel('modified_dataset.xlsx')

def fill_time_to_angio(dataframe):
    angio = dataframe.iloc[:, 0]
    angio = angio.replace({-888: np.nan})
    for ind, i in enumerate(angio):
        if not pd.isnull(i) and i <= 7:
            angio[ind] = 1
        else:
            angio[ind] = 0
    dataframe['time_to_angio'] = angio
    return

def fill_other_cols(dataframe):
    # other_elem
    other_elem = dataframe['other_elem']
    for ind, i in enumerate(other_elem):
        if not pd.isnull(i):
            other_elem[ind] = 1
        else:
            other_elem[ind] = 0
    dataframe['other_elem'] = other_elem

    # vaso_hrs
    vaso_hrs = dataframe['vaso_hrs']
    for ind, i in enumerate(vaso_hrs):
        if pd.isnull(i) or i == 888.0 or i == 999.0:
            vaso_hrs[ind] =  0
    dataframe['vaso_hrs'] = vaso_hrs

    return


fill_time_to_angio(df)
fill_other_cols(df)