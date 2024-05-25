# -*- coding: utf-8 -*-
from openai import OpenAI
import numpy as np
import pandas as pd

client = OpenAI(
    api_key="sk-K9QGaTdbLnrs4ux3t1zFZQJ41osq8lYQ",
    base_url="https://api.proxyapi.ru/openai/v1",
)

#function to make embeding from text
def get_embedding(text):
    model="text-embedding-ada-002"
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding


#find content_name text in campaign promt
def find_content_name_in_promt():

    #read campaign_promt
    with open('campaign_promt.txt', 'r',encoding='utf-8') as file:
        # Read the entire file content into a single string
        content = file.read()
        content = content.replace('\n', ' ')
    promt_to_get_content_name_name = '"'+ content + '"' + ' -Это описание маркетинговой кампании. Пожлауйста верни только название шаблона из нее на русском языке. Важно только название шаблона без лишних слов. В названии шаблона также укажи один из каналов SMS ,Email, Push '
    chat_completion = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "system", "content": promt_to_get_content_name_name}]
    )



    promt_content_name = chat_completion.choices[0].message.content
    return promt_content_name

promt_content_name = find_content_name_in_promt()
promt_content_embedding = get_embedding(promt_content_name)

def find_simmilar_content_num(promt_content_embedding):
    content_embedding_table =  '03 df_content_embedding.json'
    df_content_embedding = pd.read_json(content_embedding_table)
    df_content_embedding['sim_score']= df_content_embedding.apply(lambda x: np.dot(x['embedding'],promt_content_embedding), axis=1)
    target_content = int(df_content_embedding.iloc[[df_content_embedding['sim_score'].idxmax()]]['Content_id'].iloc[0])
    target_content_sim_score = df_content_embedding.iloc[[df_content_embedding['sim_score'].idxmax()]]['sim_score'].iloc[0]
    return target_content , target_content_sim_score

target_content , target_content_sim_score = find_simmilar_content_num(promt_content_embedding)

import sys

sys.stdout.reconfigure(encoding='utf-8')
print(target_content)  # This prints the result which will be captured by script1.py




