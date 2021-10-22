import os
from glob import glob

#this code need only on windows but for linux just execute "dvc add Training_Batch_Files/*.csv Prediction_Batch_files/*.csv" on terminal
data_dirs = ['Prediction_Batch_files', 'Training_Batch_Files']
for data_dir in data_dirs:
    files = glob(data_dir+r'/*.csv')
    for filepath in files:
        os.system(f'dvc add {filepath}')