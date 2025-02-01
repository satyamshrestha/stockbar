# SHARESANSAR

from bs4 import BeautifulSoup
import requests

url = BeautifulSoup("https://www.sharesansar.com/live-trading", "html.parser")
soup = requests.get(url)
soup = BeautifulSoup(soup.text, 'lxml')
table = soup.table
rows = table.find_all('tr')

data = []
header_row = rows[0]
column_name = [header.text for header in header_row.find_all('th')]
data.append(column_name)

for row in rows[1:]:
    columns = row.find_all('td')
    if len(columns) > 0:
        row_data = [column.text.strip() for column in columns]
        data.append(row_data)

import csv
file = open("share_data.csv", "w")
s = csv.writer(file)
s.writerows(data)
file.close()

import pandas as pd 
df = pd.read_csv("share_data.csv")

Symbol = list(df["Symbol"])[0:8]
LTP = df["LTP"]
LTP = list(map(lambda x:float(x.replace(",", "")), LTP))[0:8]


import plotly.graph_objects as go
fig = go.Figure([go.Bar(x=Symbol, y=LTP)])
fig.show()