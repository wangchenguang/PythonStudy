import pandas as pd
from pandas import Series, DataFrame

bikes = DataFrame(pd.read_excel('C:\\Users\\wangc\\Desktop\\bike.xlsx'))
bikes.to_excel('C:\\Users\\wangc\\Desktop\\bike_bak.xlsx')
print(bikes)
