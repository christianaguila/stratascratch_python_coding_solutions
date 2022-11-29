""" Highest Salary In Department

Find the employee with the highest salary per department.
Output the department name, employee's first name along with the corresponding salary. """

# Import your libraries
import pandas as pd

# Start writing code
df = employee.copy()
df[df['salary'] == df.groupby('department')['salary'].transform('max')][['first_name', 'department', 'salary']]

