""" Top Ranked Songs

Find songs that have ranked in the top position. Output the track name and the number of times it ranked at the 
top. Sort your records by the number of times the song was in the top position in descending order. """

# Import your libraries
import pandas as pd

# Start writing code
df = spotify_worldwide_daily_song_ranking
df[df['position'] == 1].groupby('trackname', as_index=False).count()[['trackname',
    'position']].sort_values('position', ascending=False).rename(columns={'position': 'top_count'})