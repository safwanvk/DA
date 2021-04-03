import pandas as pd

# Read CSV
df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/weather_data.csv')
print(df)

# Read Excel
df = pd.read_excel('/home/safwan/Documents/projects/python/Data Analysis/pandas/weather_data.xlsx')
print(df)

#From dict
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
print(df)

#From List of Tuple
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(weather_data, columns=['day','temperature','windspeed','event'])
print(df)

#From List of Dict
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'}
]
df = pd.DataFrame(weather_data)
print(df)


# another methods
# pd.read_html
# pd.read_json
# pd.read_sql
