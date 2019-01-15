import pandas as pd
from pandas import DataFrame

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
# 创建表数据机构
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYuan', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
print(df2)
df2 = df2.drop(index=['ZhangFei'])
print(df2)
