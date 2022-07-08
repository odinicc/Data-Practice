from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

def parse_banks(web_link):
    page = urlopen(web_link)
    soup = BeautifulSoup(page, 'html.parser')
    data = pd.DataFrame(columns=["Num","Name", "Market Cap (US$ Billion)"])
    for row in soup.find_all('tbody')[3].find_all('tr'):
        col = row.find_all('td')
        if row.text:
            st = str(row.text)
            s = st.split()
            Num = s[0]
            Name = s[1:-1]
            Full_name = ' '.join(Name)
            Cap = s[-1]
            l = len(s)
            #print(Num,Full_name , Cap)
            if Num != 'Rank':
                df2 = {'Num': Num, 'Name': Full_name, 'Market Cap (US$ Billion)': Cap}
                data = data.append(df2, ignore_index = True)
    return data

web_link = "https://en.wikipedia.org/wiki/List_of_largest_banks"
data = parse_banks(web_link)
print(data.to_string(index=False))
data.to_json('data.json')



