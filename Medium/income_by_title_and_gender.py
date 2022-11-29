""" Income By Title and Gender

Find the average total compensation based on employee titles and gender. Total compensation is calculated by 
adding both the salary and bonus of each employee. However, not every employee receives a bonus so disregard 
employees without bonuses in your calculation. Employee can receive more than one bonus. Output the employee 
title, gender (i.e., sex), along with the average total compensation.
 """

# Import your libraries
import pandas as pd

# Start writing code
sf_employee.merge(sf_bonus, left_on='id', right_on='worker_ref_id').groupby(['id', 'employee_title', 'sex', 'salary'],
 as_index=False).agg({'bonus': 'sum'}).assign(total_compensation = lambda x: x['salary'] + 
 x['bonus']).groupby(['employee_title', 'sex'], as_index=False)['total_compensation'].mean()