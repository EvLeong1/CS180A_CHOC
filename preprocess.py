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

hemoglobin_levels.apply(graph_change, axis=1)
plt.show()

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