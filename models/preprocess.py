# Preprocessing file
# pip install openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('capstone_dataset.xlsx')

hemoglobin_levels = df.loc[:, 'hb1':'time21']
hb_cols = [col for col in hemoglobin_levels if 'hb' in col]

hb_df = hemoglobin_levels[hb_cols]
hb_stats = pd.DataFrame(hb_df)

# Calculate average rate of change for hemoglobin for each patient
def hb_roc(row):
    rates = []
    for i in range(len(row)-1):
        if not pd.isnull(row[i]) and not pd.isnull(row[i+1]):
            rates.append((row[i+1]-row[i])/row[i])
    return np.mean(rates) if rates else np.nan

hb_stats['avg_rate_of_change'] = hb_df.apply(hb_roc, axis=1)

def graph_change(row):
    graph = []
    for i, j in zip(range(0, len(row)-1, 2), range(1, len(row), 2)):
        if not pd.isnull(row[i]) and not pd.isnull(row[j]) and row[i]!=999.0 and row[j]!=999.0 and row[i]!=888.0 and row[j]!=888.0:
            graph.append((row[i], row[j]))
    plt.plot(graph)

#hemoglobin_levels.apply(graph_change, axis=1)
# plt.show()

# pd.set_option('display.max_rows', None)  # Uncomment to show all rows
# Return a standarized dataframe where hb levels are conformed to their post-injury times
def standarize_hb(dataframe):
    dataframe.replace('#NULL!', np.nan, inplace=True) # Replace #NULL! values with NaN
    std_df = pd.DataFrame()
    time_intervals = [(i, round(i + 4.99, 2)) for i in range(0, 76, 5)] # 0 to 75 hours post-injury in intervals of 5

    for interval in time_intervals:
        start_time, end_time = interval
        interval_hb_values = []  # List to store hemoglobin levels within the interval for all patients

        for index, row in dataframe.iterrows():
            patient_hb_values = []  # List to store hemoglobin levels within the interval for the current patient

            for count in range(1, 38): # Iterate through time columns for the current patient to check if the time falls within the current interval and the hemoglobin level is not null
                if start_time <= row[f'time{count}'] <= end_time and not np.isnan(row[f'hb{count}']):
                    patient_hb_values.append(row[f'hb{count}'])

            mean_hb_level = np.mean(patient_hb_values) if patient_hb_values else np.nan # Calculate the mean hemoglobin level for the patient within the interval
            interval_hb_values.append(mean_hb_level)

        std_df[f'hb_{start_time}-{end_time}'] = interval_hb_values

    return std_df
# Print standarized dataframe
# print(standarize_hb(df))

def modified_dataset(dataframe):
    df_copy = dataframe.copy()
    df_copy = df_copy.iloc[:, :-171]
    del_cols = ['id', 'redcap_data_access_group', 'mo_injury', 'yr_injury', 'demographics_complete', 'hxtrauma_days',
                'moi_other', 'admit', 'injury_characteristics_and_admission_complete', 'scores_complete', 'labs_complete',
                'prbc_24osh', 'prbc_osh', 'prbc_24ptc', 'prbc_ptc', 'ffp_24osh', 'ffp_osh', 'ffp_24ptc', 'ffp_ptc',
                'platelets_24osh', 'platelets_osh', 'platelets_24ptc', 'platelets_ptc', 'blood_products_complete',
                'embo_reason', 'embo_type___1', 'embo_type___2', 'embo_type___3', 'embo_type___888', 'embo_other',
                'embo_tech___1', 'embo_tech___1', 'embo_tech___2', 'embo_tech___3', 'embo_tech___4', 'embo_tech___888',
                'embo_techother', 'radiology_complete', 'dpl', 'exlap_damage', 'lap_hrs', 'lap_open', 'exlap_lap_purpose',
                'percu_drain', 'percu_hrs', 'percu_fluid___0', 'percu_fluid___1', 'percu_fluid___2', 'percu_fluid___3',
                'percu_fluid___4', 'percu_fluid___5', 'percu_fluid___6', 'percu_fluid___7', 'percu_fluid___888',
                'percu_fluid_other', 'percu_performed', 'percu_performed_other', 'percu_us', 'other_procedure_describe',
                'procedures_complete', 'missed_ii', 'describe_ii', 'describe_any', 'missed_treatment', 'ards_vent', 'reor_operation',
                'trans_reaction', 'outcomes_complete', 'time_ed', 'sbp_lowed', 'dbp_lowed', 'hr_lowed', 'hr_highed', 'vasos_other', 
                'which_ed___888', 'vitals_complete', 'transfusion_hrs', 'transfusion_local', 'fast_results', 'exlap_hrs', 'procedure_other',
                'describe_iai', 'describe_treatment', 'comps_other', 'infection_other', 'cause_death', 'cause_other', 'stable_notprotocol',
                'stable_deviation', 'stable_deviation_describe']
    readd_cols = ['hgt', 'bmi', 'firsttemp_ptc', 'lowtemp_ptc']

    df_copy.drop(df_copy.columns[91:165], axis=1, inplace=True)
    df_copy.drop(columns=del_cols, inplace=True)
    
    for col in readd_cols:
        df_copy[col] = dataframe[col]
    df_copy.replace('#NULL!', np.nan, inplace=True)

    return pd.concat([df_copy, standarize_hb(df)], axis=1)

new_dataset = modified_dataset(df)
new_dataset.to_csv('modified_dataset.csv', index=False)
new_dataset.to_excel('modified_dataset.xlsx', index=False)