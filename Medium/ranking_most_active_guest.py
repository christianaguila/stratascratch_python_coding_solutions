""" Ranking Most Active Guests

Rank guests based on the number of messages they've exchanged with the hosts. Guests with the same number of 
messages as other guests should have the same rank. Do not skip rankings if the preceding rankings are identical.
Output the rank, guest id, and number of total messages they've sent. Order by the highest number of total 
messages first. """


# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_contacts.groupby(['id_guest'], as_index=False)['n_messages'].sum().sort_values('n_messages', ascending=False)
df['rank'] = df['n_messages'].rank(ascending=False, method='dense')
df