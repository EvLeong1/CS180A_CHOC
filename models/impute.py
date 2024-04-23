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

def fill_iss_cols(dataframe):
    start_row = 1
    end_row = 1007
    start_col = 'iss'
    end_col = 'ais_external'
    curr_iss = 888.0
    
    iss_cols = dataframe['iss']
    ais_head = dataframe['ais_head']
    ais_chest = dataframe['ais_chest']
    ais_face = dataframe['ais_face']
    ais_abdomen = dataframe['ais_abdomen']
    ais_extremity = dataframe['ais_extremity']
    ais_external = dataframe['ais_external']

    selected_section = dataframe.loc[start_row:end_row, start_col:end_col]
    for column in dataframe.columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')

    for ind, i in enumerate(iss_cols):
        if pd.isnull(i) or i == 888.0 or i == 8888.0:
            iss_cols[ind] =  0
    dataframe['iss_cols'] = iss_cols

    for ind, i in enumerate(ais_head):
        if pd.isnull(i) or i == 888.0 or i == 8888.0:
            ais_head[ind] =  0
    dataframe['ais_head'] = ais_head

    for ind, i in enumerate(ais_chest):
        if pd.isnull(i) or i == 888.0 or i == 8888.0:
            ais_chest[ind] =  0
    dataframe['ais_chest'] = ais_chest

    for ind, i in enumerate(ais_face):
        if pd.isnull(i) or i == 888.0 or i == 8888.0:
            ais_face[ind] =  0
    dataframe['ais_face'] = ais_face

    for ind, i in enumerate(ais_abdomen):
        if pd.isnull(i) or i == 888.0 or i == 8888.0:
            ais_abdomen[ind] =  0
    dataframe['ais_abdomen'] = ais_abdomen

    for ind, i in enumerate(ais_extremity):
        if pd.isnull(i) or i == 888.0 or i == 8888.0:
            ais_extremity[ind] =  0
    dataframe['ais_extremity'] = ais_extremity

    for ind, i in enumerate(ais_external):
        if pd.isnull(i) or i == 888.0 or i == 8888.0:
            ais_external[ind] =  0
    dataframe['ais_external'] = ais_external

    for i, row in selected_section.iterrows():
        print(f"Row {i}: ")
        for col, value in row.items():
            if col == selected_section.columns[0]:
                if pd.isnull(i) or i == 888.0:
                    curr_iss = 0
                    iss_cols[i] = curr_iss
                curr_iss = value
                continue
            print(f"Column {col}: {value}")
        top3_values = dataframe.apply(lambda row: row.nlargest(3).tolist(), axis=1)
        curr_sum_of_three = sum(x ** 2 for sublist in top3_values for x in sublist if x is not None)

        curr_iss = curr_sum_of_three
        if curr_iss <= 75:
            iss_cols[i] = curr_iss 
        
#TODO uncomment when fixed
#fill_iss_cols(df)
fill_time_to_angio(df)
fill_other_cols(df)