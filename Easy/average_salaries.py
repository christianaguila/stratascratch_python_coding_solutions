""" Average Salaries

Compare each employee's salary with the average salary of the corresponding department.
Output the department, first name, and salary of employees along with the average salary of that department.
 """
# Import your libraries
import pandas as pd

# Start writing code
dept_avg_salary = employee.groupby('department', as_index=False).agg({'salary': 'mean'})

employee.merge(dept_avg_salary, on='department')[['department', 'first_name', 'salary_x', 
    'salary_y']].rename(columns={'salary_x': 'salary', 'salary_y': 'average_department_salary'})