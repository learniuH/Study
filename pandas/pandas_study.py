import pandas as pd

############################################## pandas 数据结构 Series ##############################################

# 产生最简单的数据类型 series
s1 = pd.Series(['weather', 'food', 'city'])
'''
0    weather
1       food
2       city
dtype: object
'''

# 创建一个具有标签索引的 series
s2 = pd.Series(['weather', 'food', 'city'], index=['first', 'second', 'third'])
'''
first     weather
second       food
third        city
dtype: object
'''

# 使用 python 字典创建 series
sdata = {'first': 'weather', 'second': 'food', 'third': 'city'}
s3 = pd.Series(sdata)

# 根据索引标签查询数据
s3['second']   # food

# 查询多个数据
s3[['first', 'third']]
'''
first    weather
third       city
'''

############################################## pandas 数据结构 DataFrmae ##############################################

# 根据多个字段创建 DataFrame 
data = {
    'city': ['beijing', 'yunnan', 'zhejiang', 'sichuan'],
    'weather': ['12°C', '20°C', '24°C', '26°C'],
    'province': ['beijing', 'kunming', 'hangzhou', 'chengdu']
}
df1 = pd.DataFrame(data)
'''
       city weather  province
0   beijing    12°C   beijing
1    yunnan    20°C   kunming
2  zhejiang    24°C  hangzhou
3   sichuan    26°C   chengdu
'''

# 查询 DataFrame 的一列, 返回的是一个 series
df1['province']
'''
0     beijing
1     kunming
2    hangzhou
3     chengdu
'''

# 查询多列, 返回的是一个 DataFrame
df1[['city', 'weather']]
'''
       city weather
0   beijing    12°C
1    yunnan    20°C
2  zhejiang    24°C
3   sichuan    26°C
'''

# 查询一行, 结果是一个 pd.Series
df1.loc[1]
'''
city         yunnan
weather        20°C
province    kunming
Name: 1, dtype: object
'''

# 查询多行, 结果是一个 DataFrame
df1.loc[2: 3]
'''
       city weather  province
2  zhejiang    24°C  hangzhou
3   sichuan    26°C   chengdu
'''

# 查询特定区域
df = df1.loc[1: 2, 'city': 'weather']
'''
       city weather
1    yunnan    20°C
2  zhejiang    24°C
'''

############################################## pandas 查询数据 ##############################################
data = {
    'grade': ['primary', 'junior', 'senior', 'college'],
    'age': [7 ,13, 16, 19],
    'height': [100, 120, 140, 170],
    'weight': [45, 50, 55, 60]
}
df = pd.DataFrame(data)
'''
     grade  age  height  weight
0  primary    7     100      45
1   junior   13     120      50
2   senior   16     140      55
3  college   19     170      60
'''

# 使用单个 label 查询数据
df.loc[0, 'height']  # 100

df.loc[0, ['grade', 'weight']]  # 返回的是 Series
'''
grade     primary
weight         45
Name: 0, dtype: object
'''

# 使用值列表批量查询
df.loc[[1,2], 'age']  # 返回的是 Series
'''
1    13
2    16
Name: age, dtype: int64
'''

df.loc[[1, 3], ['weight', 'grade']] # 返回的是 DataFrame
'''
   weight    grade
1      50   junior
3      60  college
'''

# 使用数值区间进行范围查询
# 行 index 按区间
df.loc[0:2, 'weight']       # 返回的是 Series
'''
0    45
1    50
2    55
'''

# 列 index 按区间
df.loc[3, 'grade': 'weight'] # 返回的是 Series
'''
grade     college
age            19
height        170
weight         60
Name: 3, dtype: object
'''

# 行和列都按区间查询
df.loc[0: 2, 'grade': 'height']
'''
     grade  age  height
0  primary    7     100
1   junior   13     120
2   senior   16     140
'''

# 使用条件表达式查询
# 查询年龄小于8岁的列表
df.loc[df['age'] < 8, :]
'''
     grade  age  height  weight
0  primary    7     100      45
'''

# 查询年龄大于8岁小于16岁的列表
df.loc[(df['age'] > 8) & (df['age'] < 16), :]
'''
    grade  age  height  weight
1  junior   13     120      50
'''

# 使用函数查询
df.loc[lambda df : (df['age'] > 8) & (df['age'] < 16), :]

############################################## pandas 新增数据列/数据统计函数 ##############################################

# https://gitee.com/slient_7/study-pandas/blob/master/file/notes/3.Pandas%E6%96%B0%E5%A2%9E%E6%95%B0%E6%8D%AE%E5%88%97.ipynb


############################################## pandas 对缺失值的处理 ##############################################
df = pd.read_excel('./pandas_study.xlsx')
'''
       name  subject  grade
0    liubei  Chinese   60.0
1       NaN     math  100.0
2       NaN  English   90.0
3    guanyu  Chinese   80.0
4       NaN     math    NaN
5       NaN  English   90.0
6  zhangfei  Chinese    NaN
7       NaN     math   60.0
8       NaN  English    NaN
'''

# 检测空值
df.isnull()
'''
    name  subject  grade
0  False    False  False
1   True    False  False
2   True    False  False
3  False    False  False
4   True    False   True
5   True    False  False
6  False    False   True
7   True    False  False
8   True    False   True
'''

df['grade'].isnull()
'''
0    False
1    False
2    False
3    False
4     True
5    False
6     True
7    False
8     True
Name: grade, dtype: bool
'''

df['name'].notnull()
'''
0     True
1    False
2    False
3     True
4    False
5    False
6     True
7    False
8    False
Name: name, dtype: bool
'''

# 筛选没有空名字的所有行
df.loc[df['name'].notnull(), :]
'''
       name  subject  grade
0    liubei  Chinese   60.0
3    guanyu  Chinese   80.0
6  zhangfei  Chinese    NaN
'''

# 将分数列为空的填充为零分
df.fillna({'grade': 0})
# 等同于
df.loc[:, 'grade'] = df['grade'].fillna(0)
'''
       name  subject  grade
0    liubei  Chinese   60.0
1       NaN     math  100.0
2       NaN  English   90.0
3    guanyu  Chinese   80.0
4       NaN     math    0.0
5       NaN  English   90.0
6  zhangfei  Chinese    0.0
7       NaN     math   60.0
8       NaN  English    0.0
'''

# 将姓名的缺失值填充
df.loc[:, 'name'] = df['name'].fillna(method='ffill')
'''
       name  subject  grade
0    liubei  Chinese   60.0
1    liubei     math  100.0
2    liubei  English   90.0
3    guanyu  Chinese   80.0
4    guanyu     math    0.0
5    guanyu  English   90.0
6  zhangfei  Chinese    0.0
7  zhangfei     math   60.0
8  zhangfei  English    0.0
'''

# 将处理过的 Excel 保存
#df.to_excel('pandas_study.xlsx', index=False)

############################################## pandas 数据排序 ##############################################

# https://gitee.com/slient_7/study-pandas/blob/master/file/notes/6.Pandas%E6%95%B0%E6%8D%AE%E6%8E%92%E5%BA%8F.ipynb

############################################## pandas 字符串操作 ##############################################
data = {
    'grade': ['primary', 'junior', 'senior', 'college'],
    'age': [7 ,13, 16, 19],
    'height': [100, 120, 140, 170],
    'weight': [45, 50, 55, 60],
    'date': ['2024-11-01', '2023-12-01', '2024-09-01', '2025-10-01']
}
df = pd.DataFrame(data)

# 判断是不是数字, 注意只能在字符串列上使用
df['grade'].str.isnumeric()
'''
0    False
1    False
2    False
3    False
'''
# 否则像这样的会报错: AttributeError: Can only use .str accessor with string values!
# df['age'].str.isnumeric()

# 使用 startswith 做条件查询
condition = df.loc[:, 'date'].str.startswith('2024')
'''
0     True
1    False
2     True
3    False
Name: date, dtype: bool
'''
df[condition]
'''
     grade  age  height  weight        date
0  primary    7     100      45  2024-11-01
2   senior   16     140      55  2024-09-01
'''

# 将字符串中的 - 去除
df['date'].str.replace('-', '')
'''
0    20241101
1    20231201
2    20240901
3    20251001
'''

############################################## pandas axis参数 ##############################################
import numpy as np
df = pd.DataFrame(
    np.arange(12).reshape(3,4),    # 0-11 按照 3行4列排序
    columns= ['A', 'B', 'C', 'D']
)
'''
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

# axis=1 代表着删除某列, 也可以写成 axis='columns'
df.drop('A', axis='columns')
'''
   B   C   D
0  1   2   3
1  5   6   7
2  9  10  11
'''

# axis=0 代表着删除某一行, 也可以写成 axis='index'
df.drop(1, axis='index')
'''
   A  B   C   D
0  0  1   2   3
2  8  9  10  11
'''

############################################## pandas 索引index ##############################################
data = {
    'city': ['beijing', 'yunnan', 'zhejiang', 'sichuan'],
    'weather': ['12°C', '20°C', '24°C', '26°C'],
    'province': ['beijing', 'kunming', 'hangzhou', 'chengdu']
}
df = pd.DataFrame(data)
'''
       city weather  province
0   beijing    12°C   beijing
1    yunnan    20°C   kunming
2  zhejiang    24°C  hangzhou
3   sichuan    26°C   chengdu
'''

# 使用 index 查询数据
df.set_index('city', inplace=True, drop=False)
'''
              city weather  province
city
beijing    beijing    12°C   beijing
yunnan      yunnan    20°C   kunming
zhejiang  zhejiang    24°C  hangzhou
sichuan    sichuan    26°C   chengdu
'''

df.loc['beijing']
'''
city        beijing
weather        12°C
province    beijing
Name: beijing, dtype: object
'''

df.loc[df['city'] == 'beijing']
'''
            city weather province
city
beijing  beijing    12°C  beijing
'''



print(df1)