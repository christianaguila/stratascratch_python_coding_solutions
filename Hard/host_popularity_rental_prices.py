""" Host Popularity Rental Prices


You’re given a table of rental property searches by users. The table consists of search results and outputs host information for searchers. Find the minimum, average, maximum rental prices for each host’s popularity rating. The host’s popularity rating is defined as below:
0 reviews: New
1 to 5 reviews: Rising
6 to 15 reviews: Trending Up
16 to 40 reviews: Popular
more than 40 reviews: Hot


Tip: The id column in the table refers to the search ID. You'll need to create your own host_id by concating price, room_type, host_since, zipcode, and number_of_reviews.


Output host popularity rating and their minimum, average and maximum rental prices.
 """

# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_host_searches.copy()
df['host_id'] = df[['price','room_type', 'host_since', 'zipcode', 'number_of_reviews']].apply(lambda x: "_".join(x.astype(str)), axis=1)
df2 = df[['host_id', 'price', 'number_of_reviews']].drop_duplicates()
df2['host_popularity'] = df2['number_of_reviews'].apply(lambda x: 'New' if x==0 else 'Rising' if x>=1 and x<=5 else 'Trending Up' if x>=6 and x<=15 else 'Popular' if x>=16 and x<=40 else 'Hot')
df2.groupby('host_popularity', as_index=False).agg({'price': ['min', 'mean', 'max']})