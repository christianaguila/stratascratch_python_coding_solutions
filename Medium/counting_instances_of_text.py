""" Counting Instances in Text

Find the number of times the words 'bull' and 'bear' occur in the contents. We're counting the number of times 
the words occur so words like 'bullish' should not be included in our count. Output the word 'bull' and 'bear' 
along with the corresponding number of occurrences.
 """

# Import your libraries
import pandas as pd

# Start writing code
google_file_store['contents'] = google_file_store['contents'].str.split(" ")
df = google_file_store.explode('contents')
df[(df['contents'] == 'bull')|(df['contents'] == 'bear')]['contents'].value_counts().reset_index().rename(
    columns={'index':'word', 'contents':'count'})