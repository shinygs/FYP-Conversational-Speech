##!/usr/bin/env python3

# Author: Suthakar Shiny Gladdys
# Date Last Modified: 22/2/2022

import sys, os
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import pandas as pd


model_name = 'tuner007/pegasus_paraphrase'
# torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch_device = 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

def gen_sim_sent(df, num):
    sent_list = df['sentence'].tolist()
    df2 = pd.DataFrame(columns=['query_sentence','similar_sentence'])

    for ind, elmt in enumerate(sent_list):
        try:
            gen_list = []
            gen_list = pegasus_model(elmt, int(num))
            for j in gen_list:
                df2 = df2.append({'query_sentence': elmt, 'similar_sentence': j}, ignore_index=True)

            print('At query sentence no. ' + str(ind+1))
        except:
            print(elmt + " - has error")

    return df2

 
def pegasus_model(input_text,num_return_sequences):
  batch = tokenizer.prepare_seq2seq_batch([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=60,num_beams=10, num_return_sequences=num_return_sequences, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text


file_path = sys.argv[1]
num_sim_sent = sys.argv[2]
os.chdir(os.path.dirname(file_path))
new_file_path = os.path.join(os.getcwd(), 'similar_sentences_pegasus' + '.csv')
file_df = pd.read_csv(file_path)
result_df = gen_sim_sent(file_df, num_sim_sent)
result_df['query_sentence'] = result_df['query_sentence'].mask(result_df['query_sentence'].duplicated(),"")
result_df.to_csv(new_file_path, index=False)