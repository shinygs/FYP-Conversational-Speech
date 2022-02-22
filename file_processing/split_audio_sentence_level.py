import sys, os
import pandas as pd
from pydub import AudioSegment

def process_times(df):
    
    df[['times', 'sentence']] = df['data'].str.split('\t', n=1, expand=True)
    df[['start_time', 'end_time']] = df['times'].str.split(' ', n=1, expand=True)
    df.drop(['data', 'times'], axis=1, inplace=True)
    df = df[['start_time', 'end_time', 'sentence']]
    df[['st_1', 'st_2']] = df['start_time'].str.split('.', n=1, expand=True)
    df[['et_1', 'et_2']] = df['end_time'].str.split('.', n=1, expand=True)
    df['st_2'] = df['st_2'] + '0'
    df['et_2'] = df['et_2'] + '0'
    df['st_final'] = df['st_1'].astype(int)*1000 + df['st_2'].astype(int)
    df['et_final'] = df['et_1'].astype(int)*1000 + df['et_2'].astype(int)

    return df


def create_audio_by_sentence(wav_folder, wav_by_sentence_folder, name, df):
    audio = AudioSegment.from_wav(os.path.join(wav_folder, name + '.wav'))
    
    for index, row in df.iterrows():
        newAudio = audio[row.st_final:row.et_final]
        newAudio.export(os.path.join(wav_by_sentence_folder, name + '_' + str(row.st_final) + '-' + str(row.et_final) + '.wav'), format="wav")
        

folder_path = sys.argv[1]
transcripts_folder_path = os.path.join(folder_path, 'transcripts')
wav_folder_path = os.path.join(folder_path, 'wav')
wav_by_sentence_folder_path = os.path.join(folder_path, 'wav_by_sentence')
os.makedirs(wav_by_sentence_folder_path)
os.chdir(transcripts_folder_path)

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{transcripts_folder_path}\{file}"
        file_name = file[:-4]
        file_df = pd.read_csv(file_path, names=['data'])
        process_df = process_times(file_df)
        create_audio_by_sentence(wav_folder_path, wav_by_sentence_folder_path, file_name, process_df)