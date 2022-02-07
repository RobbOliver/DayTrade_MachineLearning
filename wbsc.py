from typing import List
import requests
from bs4 import BeautifulSoup

def investInd(ativo):
    ativo = ativo.lower()[:-3]+'-'+ativo.lower()[3:]

    url = "https://br.investing.com/currencies/"+str(ativo)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'}

    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.content, "html.parser")

    ttabela_bruta = soup.find('table', class_='datatable_table__2Qbdw datatable_table--border__1hROx datatable_table--freeze-column__2e8u1')
    ttabela_ = ttabela_bruta.find_all('tr', class_='datatable_row__2vgJl')

    list_indic = []
    
    # Convert to a List and Chenged Str to Int
    for item_tabela in ttabela_:
        for item_ in item_tabela:
            if item_.text == 'Venda Forte':
                list_indic.append(-2)
            elif item_.text == 'Venda':
                list_indic.append(-1)
            elif item_.text == 'Neutro':
                list_indic.append(0)
            elif item_.text == 'Compra':
                list_indic.append(1)
            elif item_.text == 'Compra Forte':
                list_indic.append(2)
            else:
                list_indic.append(item_.text)

    del(list_indic[0:6]) # Clean the data

    return list_indic