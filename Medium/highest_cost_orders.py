""" Highest Cost Orders

Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. 
If customer had more than one order on a certain day, sum the order costs on daily basis. 
Output customer's first name, total cost of their items, and the date.

For simplicity, you can assume that every first name in the dataset is unique.
 """
# Import your libraries
import pandas as pd

# Start writing code
df = customers.merge(orders, left_on='id', right_on='cust_id')
df2 = df[df.order_date.between('2019-02-01','2019-05-01')].groupby(['first_name','order_date'], as_index=False)['total_order_cost'].sum()
df2['order_date'] = df2['order_date'].dt.date
df2[df2.total_order_cost == df2.total_order_cost.max()]


# OR (Alternative Solution)

# Import your libraries
import pandas as pd

# Start writing code
df = customers.merge(orders, left_on='id', right_on='cust_id')
df2 = df[(df.order_date > pd.to_datetime('2019-02-01'))|(df.order_date < pd.to_datetime('2019-05-01'))].groupby(['first_name','order_date'], as_index=False)['total_order_cost'].sum()
df2['order_date'] = df2['order_date'].dt.date
df2[df2.total_order_cost == df2.total_order_cost.max()]