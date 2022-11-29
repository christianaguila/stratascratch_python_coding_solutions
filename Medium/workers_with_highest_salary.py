""" Workers With The Highest Salaries

Find the titles of workers that earn the highest salary. Output the highest-paid title or multiple titles that 
share the highest salary. """

# Import your libraries
import pandas as pd 


# Start writing code
df = worker.merge(title, left_on='worker_id', right_on='worker_ref_id')
df[df['salary'] == df['salary'].max()]['worker_title']