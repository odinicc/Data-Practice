import requests
import pandas as pd

Api_key = "5CjYnJS1M24sniycL7m9xrsU5yG4jP2X"
payload = {}
headers = {
    "apikey": Api_key
}
def create_df_of_rates(curr_list):
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"
    cur_l = ','.join(curr_list)
    url =url.replace("{symbols}",cur_l)
    url =url.replace("{base}","USD")

    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    result_json = response.json()
    rates = result_json['rates']
    #return dict of dates EUR:1.3
    return rates

def create_curr_list():
    url = "https://api.apilayer.com/exchangerates_data/symbols"
    response = requests.request("GET", url, headers=headers, data=payload)
    result_json_dic = response.json()
    dic_curr = result_json_dic['symbols']
    curr_list = list(dic_curr.keys())
    print("Currency list extracted")
    return dic_curr, curr_list


dic_curr, curr_list = create_curr_list()
rates = create_df_of_rates(curr_list)
df_rates = pd.DataFrame(rates.items(), columns=['Currency', 'Rate'])
print(df_rates)
df_rates.to_csv('df_rates.csv')


