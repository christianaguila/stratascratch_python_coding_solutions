""" Highest Target Under Manager

Find the highest target achieved by the employee or employees who works under the manager id 13. Output the first 
name of the employee and target achieved. The solution should show the highest target achieved under manager_id=13
and which employee(s) achieved it. """


# Import your libraries
import pandas as pd

# Start writing code
df = salesforce_employees.copy()
df[df.manager_id==13].nlargest(1, 'target', keep='all')[['first_name', 'target']]

# OR (Alternative Solution)
df = salesforce_employees.copy()
df = df[df.manager_id==13]
df[df.target == df.target.max()][['first_name', 'target']]
