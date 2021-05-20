import pandas as pd 
import plotly.express as px


df = pd.read_csv("deaths.csv")

datum = df['Date']
antal_döda = df['National_Daily_Deaths']

fig = px.line(x = datum, y = antal_döda, title = 'Antal döda under en tidsperiod', labels = {'x':'Månad', 'y':'Död'})

fig.show()





