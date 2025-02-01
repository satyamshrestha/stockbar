# WORLDOMETER

from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
soup = BeautifulSoup(soup.text,"lxml")
table_code = soup.table
tags = table_code.find_all('tr')

data = []
for tag in tags:
    x = (tag.text.split("\n"))
    if x[1] != "":
        data.append(x[1:])


import csv
file = open('covid_data.csv','w')
x = csv.writer(file)
x.writerows(data)
file.close()


import pandas as pd
df = pd.read_csv('covid_data.csv',encoding = 'latin1', index_col="#")


Country = list(df['Country,Other'])[0:5]
Total_Cases = df['TotalCases']
Total_Cases = list(map(lambda x:float(x.replace(',','')), Total_Cases))[0:5]
TotalRecovered = list(df['TotalRecovered'])[0:5]
TotalRecovered = list(map(lambda x:float(x.replace(',','')), TotalRecovered))


import plotly.graph_objects as go

fig = go.Figure([go.Bar(x=Country, y=Total_Cases)])
fig.show()

import plotly.graph_objects as go

fig = go.Figure(data = [
    go.Bar(name ='Total Cases', x = Country, y = Total_Cases),
    go.Bar(name ='Total Recovered', x = Country, y = TotalRecovered)
])
# Change the bar mode
fig.update_layout(barmode = 'group')
fig.show() 