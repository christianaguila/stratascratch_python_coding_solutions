""" Users By Average Session Time

Calculate each user's average session time. A session is defined as the time difference between a page_load 
and page_exit. For simplicity, assume a user has only 1 session per day and if there are multiple of the same 
events on that day, consider only the latest page_load and earliest page_exit. Output the user_id and their 
average session time.
 """

 
# Import your libraries
import pandas as pd

# Start writing code
df = facebook_web_log.copy()
df2 = df[df['action'].isin(['page_load','page_exit'])]
df2['date'] = df2['timestamp'].dt.date
df3 = df2[df2['action']=='page_load'].groupby(['user_id','date'], as_index=False).max()

df4 = df3.merge(df2[df2['action']=='page_exit'], on=['user_id', 'date'])
df4['duration'] = df4['timestamp_y'] - df4['timestamp_x']
df4['duration'] = df4['duration'].dt.total_seconds()
df4.groupby('user_id', as_index=False)['duration'].mean()
