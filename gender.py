import pandas as pd 
import plotly.express as px


df = pd.read_csv("Gender_Data.csv")

gender = df['Gender']
cases = df['Total_Cases']

fig = px.line(x = gender, y = cases , title = 'Antal döda under en tidsperiod', labels = {'x':'Kvinnor relativt Män', 'y':'Totala fall'})
fig = px.line()

fig.show()





