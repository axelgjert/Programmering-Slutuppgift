#Importerar nödvändiga moduler  
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np


data = pd.read_csv("Deaths.csv")
print(data.head())
print(data["National_Daily_Deaths"])


x = dataframe.National_Daily_Deats
y = dataframe.Date
plt.plot()

plt.xlabel('x')
plt.ylabel('y')
plt.title('Covid-19 dödsfall Sverige')
plt.legend()
plt.show()
