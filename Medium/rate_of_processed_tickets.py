""" Find the rate of processed tickets for each type

Find the rate of processed tickets for each type.
 """


# Import your libraries
import pandas as pd

# Start writing code
df = facebook_complaints
true_cnt = df[df.processed == True].groupby('type').agg(true_count=('processed', 'count')).reset_index()
false_cnt = df[df.processed == False].groupby('type').agg(false_count=('processed', 'count'))
true_cnt.merge(false_cnt, on='type').assign(processed_rate = lambda x: x['true_count']/(x['true_count']+
    x['false_count']))[['type', 'processed_rate']]

# OR (Alternative Solution)

# Import your libraries
import pandas as pd

# Start writing code
facebook_complaints.groupby('type', as_index=False).mean()[['type','processed']]
