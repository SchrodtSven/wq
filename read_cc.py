import pandas as pd

df_cc = pd.read_csv('kaggle/Customer_support_data.csv')
# 01/08/2023 11:13,01/08/2023 11:47
#df_cc['order_date_time'] = pd.to_datetime(df_cc['order_date_time'], '%d/%m/%Y %H:%M')
#df_cc['Issue_reported at'] = pd.to_datetime(df_cc['Issue_reported at'], '%d/%m/%Y %H:%M')

df_cc