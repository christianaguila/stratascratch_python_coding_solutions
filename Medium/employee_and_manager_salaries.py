""" Employee and Manager Salaries

Find employees who are earning more than their managers. Output the employee's first name along with the 
corresponding salary. """


# Import your libraries
import pandas as pd

# Start writing code
managers = employee[employee['id'].isin(employee['manager_id'].unique())]

df = employee.merge(managers, left_on='manager_id', right_on='id')
df[df['salary_x'] > df['salary_y']][['first_name_x', 'salary_x']]