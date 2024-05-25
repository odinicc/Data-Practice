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

#find segment text in campaign promt
def find_segment_name_in_promt():

    #read campaign_promt
    with open('campaign_promt.txt', 'r',encoding='utf-8') as file:
        # Read the entire file content into a single string
        content = file.read()
        content = content.replace('\n', ' ')
    promt_to_get_segment_name = '"'+ content + '"' + 'верни только название сегмента'
    chat_completion = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "system", "content": promt_to_get_segment_name}]
    )
    promt_segment = chat_completion.choices[0].message.content
    return promt_segment

promt_segment = find_segment_name_in_promt()

promt_segment_embedding = get_embedding(promt_segment)

def find_simmilar_segment_num(promt_segment_embedding):
    segment_embedding_table =  '02 df_segment_embedding.json'
    df_segment_embedding = pd.read_json(segment_embedding_table)
    df_segment_embedding['sim_score']= df_segment_embedding.apply(lambda x: np.dot(x['embedding'],promt_segment_embedding), axis=1)
    target_segment = int(df_segment_embedding.iloc[[df_segment_embedding['sim_score'].idxmax()]]['Segment_id'].iloc[0])
    target_segment_sim_score = df_segment_embedding.iloc[[df_segment_embedding['sim_score'].idxmax()]]['sim_score'].iloc[0]
    return target_segment , target_segment_sim_score

target_segment , target_segment_sim_score = find_simmilar_segment_num(promt_segment_embedding)


print(target_segment)  # This prints the result which will be captured by anouther script




