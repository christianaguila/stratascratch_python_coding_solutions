""" Find the base pay for Police Captains

Find the base pay for Police Captains.
Output the employee name along with the corresponding base pay. """

# Import your libraries
import pandas as pd

# Start writing code
df = sf_public_salaries
df[(df['jobtitle'].str.contains('POLICE'))&(df['jobtitle'].str.contains('CAPTAIN'))][['employeename', 'basepay']]