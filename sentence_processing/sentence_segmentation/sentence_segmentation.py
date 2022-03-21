#!/usr/bin/env python3

# Author: Suthakar Shiny Gladdys
# Date Last Modified: 13/3/2022

import sys, os
import re
import csv
import pandas as pd
import deepsegment
from deepsegment import DeepSegment # requires TensorFlow and Keras to be installed
import unidecode
from num2words import num2words
import tensorflow as tf
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

all_sent_list = []

# Map YouTube words to CMU words
yt2kaldi_word =  {
    "mdm": "madam", "mdm.": "madam", # Salutations
    "ms": "miss", "ms.": "miss",
    "mrs": "missus", "mrs.": "missus",
    "dr": "doctor", "dr.": "doctor",
    "mr": "mister", "mr.": "mister",
    "%": "percent", "#": "hashtag", "&": "and", "$": "dollar", # Symbols
    "[music]": "", "[applause]": "", "[laughs]": "", # Fillers
}

def text_normalization(sentence):
    sentence = sentence.split(' ')
    
    # Convert to lower case
    sentence = [t.lower() for t in sentence]
    
    # Align sentence with CMU words
    check_keys = yt2kaldi_word.keys()
    sentence = [(yt2kaldi_word[t] if t in check_keys else t) for t in sentence]

    # Normalize dollar sign
    for i in range(len(sentence)):
        sentence[i] = re.sub('\$([0-9]+)', '\g<1> dollars', sentence[i])

    # Normalize percentage sign
    sentence = [t.replace('%', ' percent') for t in sentence]
    
    # Normalize numbers
    for i, word in enumerate(sentence):
        if word.replace('.','',1).isdigit(): # Handle decimal places
            sentence[i] = num2words(word)

    # Strip accents from characters
    sentence = [unidecode.unidecode(t) for t in sentence]
    
    return ' '.join(sentence)


def sentence_segmentation(df):
    df = df[['sentence']]
    for index, row in df.iterrows():
        row.sentence = text_normalization(row.sentence)

    para = ''
    for index, row in df.iterrows():
        para = para + row.sentence + ' '

    segmenter = DeepSegment('en')
    sent_list = segmenter.segment_long(para)
    
    return sent_list


def write_to_new(folder, name, list):
    new_file_path = os.path.join(folder, name + '.txt')
    new_file = open(new_file_path, 'a')
    
    for sent in list:
        all_sent_list.append(sent)
        lineToWrite = sent + '\n'
        new_file.write(lineToWrite)

    new_file.close()



folder_path = sys.argv[1]
os.chdir(folder_path)
new_folder_path = os.path.join(os.path.dirname(os.getcwd()), 'segmented_text')
os.makedirs(new_folder_path)

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{folder_path}\{file}"
        file_name = file[:-4]
        file_df = pd.read_csv(file_path, names=['times', 'sentence'], delimiter='\t')
        try:
            process_list = sentence_segmentation(file_df)
            write_to_new(new_folder_path, file_name, process_list)
        except:
            print(file + ' has error')

all_sent_df = pd.DataFrame(all_sent_list, columns =['sentence'])
all_sent_df.to_csv(os.path.join(os.path.dirname(os.getcwd()), 'all_sentences.csv'), index=False)
