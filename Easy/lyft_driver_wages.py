""" Lyft Driver Wages

Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD.
Output all details related to retrieved records.
 """
 
# Import your libraries
import pandas as pd

# Start writing code
df = lyft_drivers.copy()
df[(df['yearly_salary'] <= 30000)|(df['yearly_salary'] >= 70000)]