""" Acceptance Rate By Date

What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date 
the request was sent. Order by the earliest date to latest.


Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user 
(i.e., user_id_receiver) that's logged in the table with action = 'sent'. If the request is accepted, the table 
logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.
 """


# Import your libraries
import pandas as pd

# Start writing code
df = fb_friend_requests
df2 = df[df.action=='sent'].merge(df[df.action=='accepted'], on=['user_id_sender','user_id_receiver'], how='left')
df2.groupby('date_x', as_index=False).agg({'action_x': 'count', 'action_y': 'count'}
    ).assign(acceptance_rate = lambda x: x['action_y']/x['action_x'])[['date_x', 'acceptance_rate']]