""" Salaries Differences

Write a query that calculates the difference between the highest salaries found in the marketing and 
engineering departments. Output just the absolute difference in salaries.
 """
 
# Import your libraries
import pandas as pd

# Start writing code
df = db_employee.merge(db_dept, left_on='department_id', right_on='id').groupby('department', as_index=False).agg({'salary': 'max'})

abs(df['salary'][1] - df['salary'][3])
