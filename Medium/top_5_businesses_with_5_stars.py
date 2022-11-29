""" Top 5 States With 5 Star Businesses

Find the top 5 states with the most 5 star businesses. Output the state name along with the number of 5-star 
businesses and order records by the number of 5-star businesses in descending order. In case there are ties in 
the number of businesses, return all the unique states. If two states have the same result, sort them in 
alphabetical order. """


# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business.copy()
df[df['stars'] == 5].groupby('state', as_index=False)['stars'].count().nlargest(5,  'stars', keep='all')