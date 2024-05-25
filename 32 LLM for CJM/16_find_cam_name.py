# -*- coding: utf-8 -*-
from openai import OpenAI
import numpy as np
import pandas as pd

client = OpenAI(
    api_key="sk-K9QGaTdbLnrs4ux3t1zFZQJ41osq8lYQ",
    base_url="https://api.proxyapi.ru/openai/v1",
)


#find cam_name text in campaign promt
def find_cam_name_in_promt():

    #read campaign_promt
    with open('campaign_promt.txt', 'r',encoding='utf-8') as file:
        # Read the entire file content into a single string
        content = file.read()
        content = content.replace('\n', ' ')
    promt_to_get_cam_name_name = 'дай краткое название маркетинг кампании до 50 символов по следующему описанию '+'"'+ content + '"'  
    chat_completion = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "system", "content": promt_to_get_cam_name_name}]
    )
    promt_cam_name = chat_completion.choices[0].message.content
    return promt_cam_name

promt_cam_name = find_cam_name_in_promt()

import sys

sys.stdout.reconfigure(encoding='utf-8')
print(promt_cam_name)  # This prints the result which will be captured by script1.py




