#Moduler som krävs för programmet
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.dates import DateFormatter, WeekdayLocator 
from datetime import timedelta

#Läser in en csv fil med vaccinationsstatus från nätet
df = pd.read_csv(
    'https://covid.ourworldindata.org/data/owid-covid-data.csv', 
    usecols=['date', 'location', 'total_vaccinations_per_hundred'], #"Titlar" inuti csv filen
    parse_dates=['date'])

countries = ['Sweden'] #Här väljer vi vilket land vi vill undersöka från titeln 'location'
df = df[df['location'].isin(countries)]

pivot = pd.pivot_table(
    data=df,
    index='date',
    columns='location',
    values='total_vaccinations_per_hundred',
    aggfunc='mean',
    )

pivot = pivot.fillna(method='ffill')

# Step 4: Plot all countries
fig, ax = plt.subplots(figsize=(12,8))
fig.patch.set_facecolor('#F5F5F5')    # Ändrar bakgrunden till ljusgrå
ax.patch.set_facecolor('#F5F5F5')     # Ändrar bakgrunden till ljusgrå

for country in countries:
    ax.plot(
        pivot.index,# Vad som ska vara på x-axeln
        pivot[country], # Vad som ska vara på y-axeln
        color=colors[country],# Färg
        alpha=alphas[country]# Transparency
    )
    ax.text(
        x = pivot.index[-1] + timedelta(days=2),# Var, x
        y = pivot[country].max(),# Var, y
        color = colors[country],# Färg
        s = country,# Text
        alpha=alphas[country]# Transparency
    )


#Formaterar vad som ska visas
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_locator(WeekdayLocator(byweekday=(0), interval=1)) #Vilket intervall som diagramet läser in. I vårat vall varje dag.
ax.xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)
plt.ylim(0,100)

#Fixar utseende och färger på axlarna
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#3f3f3f')
ax.spines['left'].set_color('#3f3f3f')
ax.tick_params(colors='#3f3f3f')
ax.grid(alpha=0.1)

#Namnger axlarna och ger storlek på texten
plt.ylabel('Vaccination per 100 personer', fontsize=12, alpha=0.9)
plt.xlabel('Datum', fontsize=12, alpha=0.9)
plt.title('COVID-19 Vaccinationer över Tid', fontsize=20, weight='bold', alpha=0.9)

# Visar våran graf
plt.show()