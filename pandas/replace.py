import pandas as pd
import numpy as np

df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/weather_data_replace.csv')
print(df)

# Replace value to na value - single value
new_df = df.replace(-99999, value=np.NaN)
print(new_df)

# Replace value to na value - Replacing list with single value
new_df = df.replace([-99999,-88888], value=np.NaN)
print(new_df)

# Replacing per column using a dictionary
new_df = df.replace({
    'temperature': -99999,
    'windspeed': -99999,
    'event': '0'
}, value=np.NaN)
print(new_df)

# by using mapping
new_df = df.replace({
    -99999: np.NaN,
    '0': 'Sunny'
})
print(new_df)

# Regex with dict
# when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({
    'temperature':'[A-Za-z]',
    'windspeed': '[A-Za-z]'
    },
    '', regex=True)
print(new_df)

# Replacing list with another list


df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print(df)
new_df = df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print(new_df)

