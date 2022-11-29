""" 
Count the number of user events performed by MacBookPro users 

Count the number of user events performed by MacBookPro users.
Output the result along with the event name.
Sort the result based on the event count in the descending order.
"""

# Import your libraries
import pandas as pd

# Start writing code
df = playbook_events
df[df['device'] == 'macbook pro'].groupby('event_name', as_index=False).agg({'user_id': 'count'})