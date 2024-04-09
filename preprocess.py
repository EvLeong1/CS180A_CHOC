# Preprocessing file
# pip install openpyxl
import pandas as pd
import numpy as np

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
print(hb_stats['avg_rate_of_change'])