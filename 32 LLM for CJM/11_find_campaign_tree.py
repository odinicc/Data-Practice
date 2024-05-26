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

campaign_tree_embedding_table =  '01 df_campaign_embedding.json'
df_campaign_tree_embedding = pd.read_json(campaign_tree_embedding_table)

#write all typical campaigns to list
df_campaign_tree_embedding_list = df_campaign_tree_embedding['Campaign Description'].to_list()
df_campaign_tree_embedding_str = " ; ".join(item.replace("\n", " ") for item in df_campaign_tree_embedding_list)

#read campaign_promt
with open('campaign_promt.txt', 'r',encoding='utf-8') as file:
    # Read the entire file content into a single string
    content_in_promt = file.read()
    content_in_promt = content.replace('\n', ' ')


overal_promt = 'Есть описание маркетинговой кампании' + ' "' + content_in_promt + '" ' + 'Верни наиболее близкое описание из списка стандартных кампаний'+ df_campaign_tree_embedding_str + ' Важно: Отправь пожалуйста только название кампании'

chat_completion = client.chat.completions.create(
    model="gpt-4o", messages=[{"role": "system", "content": overal_promt}]
)

chat_response = chat_completion.choices[0].message.content
chat_response_embedding = get_embedding(chat_response)

#find items in typical campaign trees similar to response
def find_simmilar_campaign_tree_num(promt_campaign_tree_embedding):
    campaign_tree_embedding_table =  '01 df_campaign_embedding.json'
    df_campaign_tree_embedding = pd.read_json(campaign_tree_embedding_table)
    df_campaign_tree_embedding['sim_score']= df_campaign_tree_embedding.apply(lambda x: np.dot(x['embedding'],promt_campaign_tree_embedding), axis=1)
    target_campaign_tree = df_campaign_tree_embedding.iloc[[df_campaign_tree_embedding['sim_score'].idxmax()]]['Campaign Tree'].iloc[0]
    target_campaign_tree_sim_score = df_campaign_tree_embedding.iloc[[df_campaign_tree_embedding['sim_score'].idxmax()]]['sim_score'].iloc[0]
    return target_campaign_tree , target_campaign_tree_sim_score

target_campaign_tree , target_campaign_tree_sim_score = find_simmilar_campaign_tree_num(chat_response_embedding)


print(target_campaign_tree)  # This prints the result which will be captured by anouther script




