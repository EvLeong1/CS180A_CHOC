import pandas as pd
import numpy as np

# Read all versions of data
original_data = pd.read_excel('capstone_dataset.xlsx')
imputed_data = pd.read_excel('imputed_dataset.xlsx')
misclass_data = pd.read_excel('misclassified_data.xlsx')

# INDEXING NOTES when reading manually:
#       Add 2 to the index column to get corresponding row
#       from misclass_data to original_data/imputed_data
#       
#       Ex:
#           misclass_data index column = 10, then
#           original_data row number = 12


''' ------------------'''
''' Input Values Here '''
# Enter desired row(s) (can be from the index column of misclassified_data.xlsx)
index_columns = [27,32,220,479,588,642,688,696,730,908]

# Enter name(s) of desired feature(s) from capstone_dataset.xlsx and/or imputed_dataset.xlsx
#   (Code will ignore missing column names 
#    i.e. no "target" column in captstone_dataset
#    or   no "exlap"  column in imputed_data)
features = ['target','iss','procedure___1', 'procedure___2', 'procedure___3', 'procedure___4', 'procedure___5', 'procedure___6', 'procedure___7',
            'procedure___8', 'procedure___9', 'procedure___10', 'procedure___11', 'procedure___12', 'procedure___0','spleen_ctblush','spleen_grade','liver_ctblush','liver_grade',
            'unstable_ed_or','los_floor']

# Set which dataset we want the resulting values from (can be both)
original = False
imputed = True
''' ------------------'''


# Helper functions
def get_results():
    ''' Gets desired features from each row
        
        Output:
        (dict, dict) where
        dict[(index,feature)] = value
    '''
    # initialize dicts
    original_dict = {}
    imputed_dict = {}

    # set up for loops
    original_columns = pd.read_excel('capstone_dataset.xlsx', nrows=0).columns
    imputed_columns = pd.read_excel('imputed_dataset.xlsx', nrows=0).columns

    for i in index_columns:
        for feat in features:
            if original:
                # check if feat is a column in original_data
                if feat in original_columns:
                    original_dict[(i,feat)] = original_data.at[i,feat]
            if imputed:
                # check if feat is a column in imputed_data
                if feat in imputed_columns:
                    imputed_dict[(i,feat)] = imputed_data.at[i,feat]

    return original_dict, imputed_dict

def print_results(data_dict, header):
    if header == 0:
        print("Original Dataset")
    else:
        print("Imputed Dataset")

    for key, value in data_dict.items():
        # Added 2 for ease of finding the row manually
        print(f"{key[0]+2}, {key[1]}, {value}")
    print()

def which_print():
    original_dict, imputed_dict = get_results()
    if original:
        print_results(original_dict, 0)
    if imputed:
        print_results(imputed_dict, 1)

def export_to_excel(data_dict, filename):
    results_df = pd.DataFrame()

    # create new columns
    results_df['code_index'] = index_columns
    results_df['excel_index'] = [i+2 for i in index_columns]
    for feat in features:
        results_df[feat] = ""

    # add data to feature columns
    old_index = -1
    i = 0
    for key, value in data_dict.items():
        new_index, feature = key
        
        if old_index == -1:
            old_index = new_index
        if old_index != new_index:
            old_index = new_index
            i += 1
        results_df.at[i, feature] = value
        #print("Adding",feature,"to",new_index,"with",value,"at row",i)
        
    # export to excel
    results_df.to_excel(filename, index=False)


def which_excel():
    original_dict, imputed_dict = get_results()
    if original:
        export_to_excel(original_dict, 'original_selected.xlsx')
    if imputed:
        export_to_excel(imputed_dict, 'imputed_selected.xlsx')

if __name__ == '__main__':
    which_print()
    which_excel()