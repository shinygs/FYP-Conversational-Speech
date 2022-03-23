#!/usr/bin/env python3

import sys, os
import pandas as pd
import deepsegment
from deepsegment import DeepSegment # requires TensorFlow and Keras to be installed
import unidecode
from num2words import num2words


# Map YouTube words to CMU words
yt2kaldi_word =  {
    "mdm": "madam", "mdm.": "madam", # Salutations
    "ms": "miss", "ms.": "miss",
    "mrs": "missus", "mrs.": "missus",
    "dr": "doctor", "dr.": "doctor",
    "mr": "mister", "mr.": "mister",
    "%": "percent", "#": "hashtag ", "&": "and", "$": "dollar", # Symbols
    "[music]": "", "[applause]": "" # Fillers
}


def text_normalization(sentence):
    sentence = sentence.replace('-', 'X') # Handle hyphen, e.g. two-hour
    sentence = sentence.split(' ')
    
    # Convert to lower case
    sentence = [t.lower() for t in sentence]
    
    # Align sentence with CMU words
    check_keys = yt2kaldi_word.keys()
    sentence = [(yt2kaldi_word[t] if t in check_keys else t) for t in sentence]
    
    # Normalize numbers
    for i, word in enumerate(sentence):
        if word.replace('.','',1).isdigit(): # Handle decimal places
            sentence[i] = num2words(word)

    # Strip accents from characters
    sentence = [unidecode.unidecode(t) for t in sentence]
    
    return ' '.join(sentence)


def sentence_segmentation(df):
    
    first_word_st = df.iloc[0,0].split(' -->')[0] # get start time of first word
    df = df.iloc[1::2] # remove redundant lines
    df = df.reset_index(drop=True)
    
    # split words together with their end times
    df['times'] = df['times'].str.split(' ') 
    s = df.apply(lambda x: pd.Series(x['times']), axis=1).stack().reset_index(level=1, drop=True)
    s.name = 'times'
    df = df.drop('times', axis=1).join(s)
    df = df[df['times'].str.contains("<") == True]
    df = df.reset_index(drop=True)
    df['times_2'] = df['times'].str.split('<')
    df.loc[:, 'word'] = df.times_2.map(lambda x: x[0])
    df.loc[:, 'end_time'] = '<' + df.times_2.map(lambda x: x[1])
    
    # get start time of each word
    df['start_time'] = df['end_time'].shift(1) 
    df['start_time'].iloc[0] = '<' + first_word_st + '>'
    df = df[['start_time', 'end_time', 'word']]
    
    # apply segmentation
    full_text = ' '.join(df["word"]) # concatenate all the words
    segmenter = DeepSegment('en') 
    sentence_list = segmenter.segment_long(full_text) 
    df2 = pd.DataFrame(columns=['sentence'])
    df2['sentence'] = sentence_list
    df2.index += 1 # index serves as sentence number
    df3 = pd.DataFrame(columns=['word_list'])
    df3['word_list'] = df2['sentence'].str.split(' ')
    s2 = df3.apply(lambda x: pd.Series(x['word_list']), axis=1).stack().reset_index(level=1, drop=True)
    s2.name = 'word_2'
    df3 = df3.drop('word_list', axis=1).join(s2)
    df3['sentence_number'] = df3.index
    df3 = df3.reset_index(drop=True)
    df3.index += 1
    
    # match words with their sentence numbers
    df4 = pd.merge(df, df3, left_index=True, right_index=True) 
    df4 = df4.drop('word_2', axis=1)
    df5 = df4.groupby('sentence_number').first() # find first and last words of each sentence
    df6 = df4.groupby('sentence_number').last()
    df5 = df5.drop(['word', 'end_time'], axis=1) # get start and end times of each sentence
    df6 = df6.drop(['word', 'start_time'], axis=1)
    df5 = pd.merge(df5, df6, left_index=True, right_index=True) 
    df2 = pd.merge(df2, df5, left_index=True, right_index=True)
    
    # text normalization
    for index, row in df2.iterrows():
        row.sentence = text_normalization(row.sentence)
        
    return df2


file_path = sys.argv[1]
os.chdir(os.path.dirname(file_path))
new_file_path = os.path.join(os.getcwd(), 'segmented_text_with_times' + '.txt')

new_file = open(new_file_path, 'a')
test_df = pd.read_csv(file_path, names = ['times'], skiprows = 3)
for index, row in sentence_segmentation(test_df).iterrows():
    lineToWrite = row.start_time + ' ' + row.end_time + '    ' + row.sentence + '\n'
    new_file.write(lineToWrite)
new_file.close()