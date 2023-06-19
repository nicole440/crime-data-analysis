import csv
import pandas as pd
import numpy as np

data = pd.read_csv('NYPD_Hate_Crimes.csv')
df = pd.DataFrame(data)
print(df.head(50))
print(df.dtypes)

# Prints list of Bias Motivation Descriptions and number of occurrences
motive = df['Bias Motive Description'].value_counts(ascending=True)
print(motive)

print(df.describe)

# Prints list of Offense Category values and number of occurrences
offense = df['Offense Category'].value_counts(ascending=True)
print(offense)


# Prints rows where Offense Category listed is Sexual Orientation
print(df[df['Offense Category'] == 'Sexual Orientation'])



