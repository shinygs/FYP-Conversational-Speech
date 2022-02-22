#!/usr/bin/env python3

import sys, os
import pandas as pd
import datetime


def time_process(df):
    df[['times', 'sentence']] = df['data'].str.split('\t', n=1, expand=True)
    df[['start_time', 'end_time']] = df['times'].str.split(' ', n=1, expand=True)
    df.drop(['data', 'times'], axis=1, inplace=True)
    df = df[['start_time', 'end_time', 'sentence']]
    df.index += 1

    # millisecond format standardizing
    df['start_time'] = df['start_time'] + '0'
    df['end_time'] = df['end_time'] + '0'

    # splitting start & end times into seconds and milliseconds
    df[['st_1', 'st_2']] = df['start_time'].str.split('.', n=1, expand=True)
    df[['et_1', 'et_2']] = df['end_time'].str.split('.', n=1, expand=True)

    # standardizing seconds to HH:MM:SS
    df.st_1 = df.st_1.astype(int)
    df.et_1 = df.et_1.astype(int)
    df = df.reindex(columns = df.columns.tolist() + ['st_1_converted','et_1_converted'])

    for row in df.itertuples():
        df.at[row.Index, 'st_1_converted'] = datetime.timedelta(seconds = row.st_1)
        df.at[row.Index, 'et_1_converted'] = datetime.timedelta(seconds = row.et_1)      

    df.st_1_converted = df.st_1_converted.astype(str)
    df.et_1_converted = df.et_1_converted.astype(str)
    df['st_1_converted'] = '0' + df['st_1_converted']
    df['et_1_converted'] = '0' + df['et_1_converted']

    # getting start & end times in SRT time format
    df['st_final'] = df['st_1_converted'] + ',' + df['st_2']
    df['et_final'] = df['et_1_converted'] + ',' + df['et_2']

    return df


def write_to_srt(folder, name, df):
    srt_file_path = os.path.join(folder, name + '.srt')
    srt_file = open(srt_file_path, 'a')
    df.index = df.index.astype(str)
    
    for index, row in df.iterrows():
        srt_file.write(index)
        srt_file.write('\n')
        srt_file.write(row['st_final'] + ' --> ' + row['et_final'] + '\n')
        srt_file.write(row['sentence'] + '\n\n')
    
    srt_file.close()


folder_path = sys.argv[1]
os.chdir(folder_path)
srt_folder_path = os.path.join(os.path.dirname(os.getcwd()), 'srt')
os.makedirs(srt_folder_path)

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{folder_path}\{file}"
        file_name = file[:-4]
        file_df = pd.read_csv(file_path, names=['data'])
        process_df = time_process(file_df)
        write_to_srt(srt_folder_path, file_name, process_df)


