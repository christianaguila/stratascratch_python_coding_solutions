""" Largest Olympics

Find the Olympics with the highest number of athletes. The Olympics game is a combination of the year and the season, and is found 
in the 'games' column. Output the Olympics along with the corresponding number of athletes.

 """

# Import your libraries
import pandas as pd

# Start writing code
olympics_athletes_events.groupby('games', as_index=False).agg({'id': 'nunique'}).sort_values('id', ascending=False).head(1)
