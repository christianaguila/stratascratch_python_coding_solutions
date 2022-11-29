""" Find how many times each artist appeared on the Spotify ranking list

Find how many times each artist appeared on the Spotify ranking list
Output the artist name along with the corresponding number of occurrences.
Order records by the number of occurrences in descending order.
 """

# Import your libraries
import pandas as pd

# Start writing code
df = spotify_worldwide_daily_song_ranking.copy()
df.groupby('artist', as_index=False).agg({'id': 'count'}).sort_values(by='id',ascending=False)