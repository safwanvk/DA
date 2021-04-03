import pandas as pd

df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/weather_data_missing.csv')
print(df)

print(type(df.day[0]))

# Convert type str into date type
df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/weather_data_missing.csv',parse_dates=['day'])
print(df) 

print(type(df.day[0]))

# Set index date value
df.set_index('day',inplace=True)
print(df)

# Handling Missinf data

# fillna()

new_df = df.fillna(0)
print(new_df)

new_df = df.fillna({
    'temperature': 0,
    'windspeed': 0,
    'event': 'no event'
})
print(new_df)

# carry forward the previous value
# method=ffill
new_df = df.fillna(method='ffill')
print(new_df)

# carry forward the next value
# method=bfill
new_df = df.fillna(method='bfill')
print(new_df)

# with index and column
# axis=0 or 'index' and axis=1 or 'columns
new_df = df.fillna(method='bfill', axis='index')
print(new_df)

new_df = df.fillna(method='bfill', axis='columns')
print(new_df)

# limit to fill data

new_df = df.fillna(method='ffill', limit=1)
print(new_df)

# interpolation
# interpolate()
# default linear. other quadratic,cubic
new_df = df.interpolate()
print(new_df)

# Consider fill data with time
new_df = df.interpolate(method='time')
print(new_df)

# Drop all the rows which has "na" in dataframe
# dropna()
new_df = df.dropna()
print(new_df)

# Drop column as all cell na
# how 
# all and any
new_df = df.dropna(how='all')
print(new_df)

# Drop atleast one no-na value
# thresh
new_df = df.dropna(thresh=1)
print(new_df)

dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df.reindex(idx)

print(df)

