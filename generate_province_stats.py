import pandas as pd
import numpy as np
import random
provinces = ["Noord-Holland","Zuid-Holland", "Zeeland", "Noord-Brabant", "Utrecht", "Flevoland", "Friesland", "Groningen", "Drenthe", "Overijssel", "Gelderland",  "Limburg"]
vaccinated = []
intensive_care = []
hospitalised = []
positive = []
reproduction = []
mortality = []

for x in range(12):
    risk_level = (random.choice([0, 1, 2, 3]))
    if risk_level == 0:
        vaccinated.append(random.randint(300000,400000))
        intensive_care.append(random.randint(0,5))
        hospitalised.append(random.randint(0,50))
        positive.append(random.randint(0,100))
        reproduction.append(random.randrange(0,10) / 10)
        mortality.append(random.randint(0,5))
    elif risk_level == 1:
        vaccinated.append(random.randint(200000,300000))
        intensive_care.append(random.randint(3,15))
        hospitalised.append(random.randint(5,70))
        positive.append(random.randint(70,500))
        reproduction.append(random.randrange(10,17) / 10)
        mortality.append(random.randint(4,10))
    elif risk_level == 2:
        vaccinated.append(random.randint(50000,150000))
        intensive_care.append(random.randint(10,20))
        hospitalised.append(random.randint(5,100))
        positive.append(random.randint(150,700))
        reproduction.append(random.randrange(10,20) / 10)
        mortality.append(random.randint(5,18))
    else:
        vaccinated.append(random.randint(1000,100000))
        intensive_care.append(random.randint(40,100))
        hospitalised.append(random.randint(150,300))
        positive.append(random.randint(1000,5000))
        reproduction.append(random.randrange(20,32)/10)
        mortality.append(random.randint(20,25))

column_names=["province","vaccinated","intensive_care","hospitalised","positive","reproduction","mortality"]
df = pd.DataFrame([provinces,vaccinated,intensive_care,hospitalised,positive,reproduction,mortality]).T
df.columns = column_names
print(df)
print(df.dtypes)
df.to_csv("provinc_stats.csv")