import pandas as pd

dict = {
    "country": ["india", "maharashtra"],
    "price": [1234, 3456]
}

b = pd.DataFrame(dict)

print(b)

#        country  price
# 0        india   1234
# 1  maharashtra   3456

s = b.drop('country',axis=1)
print(s)


data = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/Sample100.csv')
print(data)


d = data.drop('Company Name', axis=1)
print(d)

# Indexing

# Pandas Series
print(data['Serial Number'])

# Pandas DataFrame
print(data[['Serial Number']])

# access rows
print(data[0:3])

print(data.iloc[2])

b.index = ["A", "B"]
print(b.loc[['A', 'B']])

print(data.columns)

data.rename(columns = {'Serial Number': 'SN'}, inplace=True)

print(data.isnull().sum())

data = data.dropna(how='any', axis=0)
print(data.isnull().sum())

data = data.drop(data.head(0).index)

print(data.head)

data = data.drop(data.index[[0]])

print(data.head)

data['Employee Markme'] = data['Employee Markme'].replace(['Mark'], 'M')

print(data.head)


# data.filna('0', isplace=True)
# fill o into null value
