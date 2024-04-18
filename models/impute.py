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

def fill_hx_trauma(dataframe):
    # hx_trauma
    dataframe.loc[dataframe['hx_trauma'] == 888, 'hx_trauma'] = 0

    # or
    # hx_trauma = dataframe['hx_trauma']
    # for ind, i in enumerate(hx_trauma):
    #     if i == 888:
    #         hx_trauma[ind] = 0
    # dataframe['hx_trauma'] = hx_trauma

    return
'''
Loop through each patient row. If the patient's pt_status
is 1, fill unstable columns as 0. If the patient's pt_status
is 2, fill stable columns as 0.
'''
def fill_stable_unstable_cols(dataframe):
    # loop through each patient row
    # if the patient[pt_status] = 1, fill unstable cols as 0
    # if the patient[pt_status] = 2, fill stable cols as 0
    stable_elems = [
    'stable_typescreen', 'stable_nonicu',
    'stable_q2h_q4h', 'stable_bedrest',
    'stable_hb6', 'stable_hb12',
    'stable_hb24', 'stable_floor',
    'stable_diet', 'stable_ambulate',
    'stable_tounstable', 'stable_dcprotocol'
    ]
    unstable_elems = [
    'unstable_typescreen', 'unstable_crystalloid', 
    'unstable_picu', 'unstable_q6h', 
    'unstable_transfusion',	'unstable_notthreshold', 
    'unstable_rebleed', 'unstable_txprotocol']

    for index, row in dataframe.iterrows():
        if row['pt_status'] == 1:  # stable
            dataframe.loc[index, unstable_elems] = 0
        elif row['pt_status'] == 2:  # unstable
            dataframe.loc[index, stable_elems] = 0
    return

fill_time_to_angio(df)
fill_other_cols(df)
fill_hx_trauma(df)
# fill_stable_unstable_cols(df)