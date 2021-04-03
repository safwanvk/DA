import pandas as pd


df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/weather_data.csv')
print(df)


weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

df1 = pd.DataFrame(weather_data)
print(df1)

# diementions
rows, columns = df.shape
print(rows, columns)

# initial few column display(5)
print(df.head)

print(df.head(2))

# last 5 rows
print(df.tail)

print(df.tail(1))

# Slicing
print(df[2:5])

print(df[:])

# see columns
print(df.columns)

# see individual column
print(df.day) # print(df['day'])

# some columns
print(df[['day', 'event']])

# OPERATIONS

#MAX
print(df['temperature'].max())

#MEAN
print(df['temperature'].mean())

#MIN
print(df['temperature'].min())

#DESCRIBE - Statics od data
print(df.describe())

# Select data like sql
print(df[df['temperature']>32])

# Select limied field
print(df.temperature[df['temperature']>32])

print(df[df['temperature']==df.temperature.max()])
print(df[df['temperature']==df['temperature'].max()])


#INDEX
print(df.index)

df.set_index('day', inplace=True)
# inplace is change current data
print(df)

# Select specific row
print(df.loc['1/1/2017'])

df.reset_index(inplace=True)
