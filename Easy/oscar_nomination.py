""" Count the number of movies that Abigail Breslin nominated for oscar

Count the number of movies that Abigail Breslin was nominated for an oscar. """


# Import your libraries
import pandas as pd

# Start writing code
oscar_nominees[oscar_nominees['nominee'] == 'Abigail Breslin']['movie'].count()