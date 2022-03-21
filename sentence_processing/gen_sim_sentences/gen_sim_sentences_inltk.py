##!/usr/bin/env python3

# Author: Suthakar Shiny Gladdys
# Date Last Modified: 22/2/2022

import sys, os
from inltk.inltk import setup
from inltk.inltk import get_similar_sentences
import pandas as pd


setup('en')

def gen_sim_sent(df, num):
    sent_list = df['sentence'].tolist()
    df2 = pd.DataFrame(columns=['query_sentence','similar_sentence'])

    for ind, elmt in enumerate(sent_list):
        try:
            gen_list = []
            gen_list = inltk_model(elmt, int(num))
            for j in gen_list:
                df2 = df2.append({'query_sentence': elmt, 'similar_sentence': j}, ignore_index=True)
                
            print('At query sentence no. ' + str(ind+1))
        except:
            print(elmt + " - has error")

    return df2

 
def inltk_model(input_text, no_of_variants):
    code_of_language = "en"
    degree_of_aug = 0.3
    result = get_similar_sentences(input_text, no_of_variants, code_of_language, degree_of_aug)

    return result


file_path = sys.argv[1]
num_sim_sent = sys.argv[2]
os.chdir(os.path.dirname(file_path))
new_file_path = os.path.join(os.getcwd(), 'similar_sentences_inltk' + '.csv')
file_df = pd.read_csv(file_path)
result_df = gen_sim_sent(file_df, num_sim_sent)
result_df['query_sentence'] = result_df['query_sentence'].mask(result_df['query_sentence'].duplicated(),"")
result_df.to_csv(new_file_path, index=False)