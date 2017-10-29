# encoding:utf-8
import numpy as np
import pandas as pd

'''
dataframe使用示例
'''

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

#通过字典进行初始化
# df = pd.DataFrame(data)


#指明列的顺序
df = pd.DataFrame(data, columns=['year', 'state', 'pop'])
# print df

#添加行的索引
df = pd.DataFrame(data, columns=['year', 'state', 'pop'],index=['one', 'two', 'three', 'four', 'five'])
# print df
# print type(df['year'])        #df的列即series对象，可见df是由series组成的

#添加不存在的列，数据表示为NAN
df = pd.DataFrame(data, columns=['year', 'state', 'pop','exp'],index=['one', 'two', 'three', 'four', 'five'])
# print df

'''
dataframe各类属性
'''
# print df.dtypes     #使用dtypes来查看各行的数据格式
# print df.head(2)        #返回前n行
# print df.tail(2)        #返回倒数n行
# print df.index      #查看数据框的索引
# print df.columns        #查看列名用columns,dataframe属性
# print df.values     #查看数据值，用values
# print df.describe()     #查看描述性统计，用describe
# print df.T      #使用T来转置数据，也就是行列转换
# print df.sort(columns = "year")       #columns为dataframe属性


'''
各种取数据的方法
'''
# print df['year']        #按列名取列，返回series对象

# print df[['year','pop']]        #按列名取多列，返回dataframe对象

# print df[0:1]       #用切片取行，返回dataframe对象

# print df.loc['one']     #使用loc取行，返回series对象

# print df.loc['one':'three']     #使用loc取多行，返回dataframe对象

# print df.iloc[0]     #使用iloc取行，返回series对象

# print df.iloc[0:2]     #使用iloc取多行，返回dataframe对象

# print df.ix['one']      #使用ix取行，返回series对象

# print df.ix['one':'three']      #使用ix取多行，返回dataframe对象

# print df.ix[0]      #使用ix取行，返回series对象

# print df.ix[0:2]      #使用ix取多行，返回dataframe对象

# print df[df.year > 2001]        #使用表达式也可以取到某些条件的行

# print df[0:1]['year']
# print df['year'][0:1]       #通过行列索引取某个值

'''
dataframe数据类型转换为dict
'''

# print dict(df['year'])      #单列转换为字典，本质上是series对象转换为字典
# print dict(df[['year','pop']])      #多列转换为字典，本质上是dataframe转换为字典，将列名作为key，列作为value


'''
数据遍历和迭代iteration
'''


'''
for i in obj 方式，对不同数据结构不同；遍历的只是df的columns names，返回结果如下
Series : 代表值
DataFrame : 代表列label，即列名
Panel : item label
'''
#默认以列列名为索引，obj为列名
# for obj in df:
#     print df[obj]

'''
.iteriems()，对DataFrame相当于对列迭代。返回结果如下
Series: (index, value)
DataFrame : (column, Series)
Panel : (item, DataFrame)
'''
# for obj in df.iteritems():
#     print obj

'''
df.iterrow()，对DataFrame的每一行进行迭代，返回一个Tuple (index, Series)
'''
# for obj in df.iterrows():
#     print obj

'''
df.itertuples()，也是一行一行地迭代，返回的是一个Pandas对象
'''
# for obj in df.itertuples():
#     print obj

