import pandas as pd
import numpy as np

df = pd.read_excel('modified_dataset.xlsx')

'''
The most critical time for angiography is the first 7 hours. To capture this,
out of the patients that have angiography data, if they have angiography performed on them within
the first 7 hours, we impute the value as 1, else 0.
'''
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

'''
The other_elem column contains specific data on injuries suffered. If there is extra data on injuries,
we wanted to capture that by imputing a value of 1, else 0.
For the vaso_hrs column, all NULL values are filled with 0.
'''
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
        # NULL, 888 (unknown), 999 (indeterminate)
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

'''
During the preprocessing stage, hb (hemoglobin) and time columns were combined to capture intervals in a concise manner.
For any NULL values between two intervals, values were imputed by first calculating the rate of change (roc)
of hb values between the intervals. Then, each NULL cell is filled by incrementing the previous hb by the roc.
'''
def fill_hb(dataframe):
    #Only use hb interval cols
    hb = dataframe.iloc[:, dataframe.columns.get_loc('hb_0-4.99'):]
    for ind, row in hb.iterrows():
        rates = [] # Where non null values for each row are stored
        for num, i in enumerate(row):
            if pd.notnull(i):
                rates.append((i, num)) # A tuple of (hb_value, index) is appended to the rates list
        if len(rates)<=1: # If there are less than 2 values in each row, no need to do anything
            pass
        else:
            for i in range(len(rates)-1):
                # Unpack tuples for index i and i+1
                val1, ind1 = rates[i] 
                val2, ind2 = rates[i+1]
                if ind2 - ind1 > 1: # If there are null values between two intervals...
                    roc = (val2 - val1)/(ind2 - ind1) # Calculate the rate of change
                    running = val1 # Then create a running variable and continue adding the rate of change
                    for cols in range(ind1+1, ind2):
                        running += roc
                        dataframe.iloc[ind, dataframe.columns.get_loc('hb_0-4.99')+cols] = np.round(running, 2)
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

    # dataframe['iss'].fillna(0, inplace=True)
    # dataframe['ais_head'].fillna(0, inplace=True)
    # dataframe['ais_chest'].fillna(0, inplace=True)
    # dataframe['ais_face'].fillna(0, inplace=True)
    # dataframe['ais_abdomen'].fillna(0, inplace=True)
    # dataframe['ais_extremity'].fillna(0, inplace=True)
    # dataframe['ais_external'].fillna(0, inplace=True)

    # dataframe['iss'].replace(888.0, 0, inplace=True)
    # dataframe['ais_head'].replace(888.0, 0, inplace=True)
    # dataframe['ais_chest'].replace(888.0, 0, inplace=True)
    # dataframe['ais_face'].replace(888.0, 0, inplace=True)
    # dataframe['ais_abdomen'].replace(888.0, 0, inplace=True)
    # dataframe['ais_extremity'].replace(888.0, 0, inplace=True)
    # dataframe['ais_external'].replace(888.0, 0, inplace=True)

    # dataframe['iss'].replace(8888.0, 0, inplace=True)
    # dataframe['ais_head'].replace(8888.0, 0, inplace=True)
    # dataframe['ais_chest'].replace(8888.0, 0, inplace=True)
    # dataframe['ais_face'].replace(8888.0, 0, inplace=True)
    # dataframe['ais_abdomen'].replace(8888.0, 0, inplace=True)
    # dataframe['ais_extremity'].replace(8888.0, 0, inplace=True)
    # dataframe['ais_external'].replace(8888.0, 0, inplace=True)

    selected_section = dataframe.loc[start_row:end_row, start_col:end_col]
    for column in dataframe.columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')

    for ind, i in enumerate(iss_cols):
        if pd.isnull(i) or i == 888.0 or i == 8888.0 or pd.isna(i):
            iss_cols[ind] =  0
    dataframe['iss'] = iss_cols

    for ind, i in enumerate(ais_head):
        if pd.isnull(i) or i == 888.0 or i == 8888.0 or pd.isna(i):
            ais_head[ind] =  0
    dataframe['ais_head'] = ais_head

    for ind, i in enumerate(ais_chest):
        if pd.isnull(i) or i == 888.0 or i == 8888.0 or pd.isna(i):
            ais_chest[ind] =  0
    dataframe['ais_chest'] = ais_chest

    for ind, i in enumerate(ais_face):
        if pd.isnull(i) or i == 888.0 or i == 8888.0 or pd.isna(i):
            ais_face[ind] =  0
    dataframe['ais_face'] = ais_face

    for ind, i in enumerate(ais_abdomen):
        if pd.isnull(i) or i == 888.0 or i == 8888.0 or pd.isna(i):
            ais_abdomen[ind] =  0
    dataframe['ais_abdomen'] = ais_abdomen

    for ind, i in enumerate(ais_extremity):
        if pd.isnull(i) or i == 888.0 or i == 8888.0 or pd.isna(i):
            ais_extremity[ind] =  0
    dataframe['ais_extremity'] = ais_extremity

    for ind, i in enumerate(ais_external):
        if pd.isnull(i) or i == 888.0 or i == 8888.0 or pd.isna(i):
            ais_external[ind] =  0
    dataframe['ais_external'] = ais_external

    for i, row in selected_section.iterrows():
        #print(f"Row {i}: ")
        for col, value in row.items():
            if col == selected_section.columns[0]:
                if pd.isnull(i) or i == 888.0:
                    curr_iss = 0
                    iss_cols[i] = curr_iss
                curr_iss = value
                continue
            #print(f"Column {col}: {value}")
        top3_values = dataframe.apply(lambda row: row.nlargest(3).tolist(), axis=1)
        curr_sum_of_three = sum(x ** 2 for sublist in top3_values for x in sublist if x is not None)

        curr_iss = curr_sum_of_three
        if curr_iss <= 75:
            iss_cols[i] = curr_iss 

'''
Combine the target columns into a single column called 'target', which helps the model classify patients into two groups: 
those who need surgery and those who do not.
'''
def combine_target_cols(dataframe):
    target_cols = ['exlap', 'lap', 'liver_ctblush', 'spleen_ctblush']
    dataframe['target'] = dataframe[target_cols].apply(lambda row: 1 if 1 in row.values else 0, axis=1)
    dataframe.drop(columns=target_cols, inplace=True)
    return dataframe


'''
Fill all NULL values with 888 for the model to run properly since the model cannot handle NULL values.
'''

def fill_null_values(dataframe, fill_value=0):
    dataframe.fillna(fill_value, inplace=True)
    return dataframe


def check_for_death(dataframe):
    dataframe['unstable_notprotocol_other'] = dataframe['unstable_notprotocol_other'].apply(
        lambda x: 1 if x == 'death' else 888 if pd.isna(x) else 0 if x == '888' else 0
    )
    
def replace_unk(dataframe):
    dataframe.replace('unk', 888, inplace=True)
    return dataframe

def fill_999(dataframe):
    dataframe.replace(999, 0, inplace=True)
    dataframe.replace(999.0, 0, inplace=True)
    return dataframe

def convert_all_to_float(dataframe):
    problematic_columns = []
    for col in dataframe.columns:
        try:
            pd.to_numeric(dataframe[col], errors='raise')
        except ValueError:
            problematic_columns.append(col)

    for col in problematic_columns:
        dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce')

    dataframe[problematic_columns] = dataframe[problematic_columns].fillna(888).astype(float)

#TODO uncomment when fixed
fill_iss_cols(df)
fill_time_to_angio(df)
fill_other_cols(df)
fill_hx_trauma(df)
fill_hb(df)
combine_target_cols(df)
fill_stable_unstable_cols(df)
fill_null_values(df)
check_for_death(df)
replace_unk(df)
fill_999(df)
convert_all_to_float(df)
df.to_excel('imputed_dataset.xlsx', index=False)
