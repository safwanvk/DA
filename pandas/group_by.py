import pandas as pd
import matplotlib

df = pd.read_csv("/home/safwan/Documents/projects/python/Data Analysis/pandas/data/weather_by_cities.csv")
print(df)

# Group
g = df.groupby('city')
print(g)

for city, df in g:
    print(city)
    print(df)

# This is similar to SQL,
# SELECT * from weather_data GROUP BY city

# Get specific group
print(g.get_group('mumbai'))

# 1. What was the maximum temperature in each of these 3 cities?
print(g.max())

# 2. What was the average windspeed in each of these 3 cities?
print(g.mean())

# This method of splitting your dataset in smaller groups and then applying an operation (such as min or max) to get aggregate result is called Split-Apply-Combine.

# min
print(g.min())

# describe
print(g.describe())

# get size
print(g.size())

# get count
print(g.count())

# plot these group
# %matplotlib inline
g.plot()

# Group data using custom function: Let's say you want to group your data using custom function. Here the requirement is to create three groups

#     Days when temperature was between 80 and 90
#     Days when it was between 50 and 60
#     Days when it was anything else

# For this you need to write custom grouping function and pass that to groupby

def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] <= 60:
        return '50-60'
    else:
        return 'others'



g = df.groupby(lambda x: grouper(df, x, 'temperature'))
print(g)


for key, d in g:
    print("Group by Key: {}\n".format(key))
    print(d)

