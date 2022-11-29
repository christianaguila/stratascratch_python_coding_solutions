""" Reviews of Categories

Find the top business categories based on the total number of reviews. Output the category along with the total 
number of reviews. Order by total reviews in descending order. """

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business.copy()
df['categories'] = df['categories'].str.split(';')
df.explode('categories').groupby('categories', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)