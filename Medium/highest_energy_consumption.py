""" Highest Energy Consumption

Find the date with the highest total energy consumption from the Meta/Facebook data centers. 
Output the date along with the total energy consumption across all data centers.
 """

# Import your libraries
import pandas as pd

# Start writing code
df=pd.concat([fb_eu_energy,fb_asia_energy,fb_na_energy], ignore_index=True).groupby('date', as_index=False).sum()
df['rank'] = df['consumption'].rank(method='dense', ascending=False)
df[df['rank'] == 1][['date', 'consumption']]