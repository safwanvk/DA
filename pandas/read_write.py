import pandas as pd

df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.csv')
print(df)


# Skip rows
df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.csv', skiprows=1)
print(df)

df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.csv', header=1)
print(df)

# Import data with null header
df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.csv', header=None, names=['tickets','eps','revenue','price','people'])
print(df)

# Limit value
df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.csv', nrows=2)
print(df)

# Clean up
df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.csv', na_values=['not available', 'n.a.'])
print(df)

# With dict
df = pd.read_csv('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.csv', na_values={
    'eps': ['not available', 'n.a.'],
    'revenue': ['not available', 'n.a.', '-1'],
    'price': ['not available', 'n.a.']
})

# Write csv
df.to_csv('data/new_data.csv')
# Remove index
df.to_csv('data/new_data.csv', index=False)

# Remove Header
df.to_csv('data/new_data.csv', header=False)

#Limit data to csc
df.to_csv('data/new_data.csv', columns=['tickers','eps'],index=False)

#############EXCEL####################
# Read
df = pd.read_excel('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.xlsx')
print(df)

#Convert data

def people_cell_convert(cell):
    if cell == 'n.a.':
        return 'haty'
    return cell

def price_cell_convert(cell):
    if cell == 'n.a.':
        return 50
    return cell

df = pd.read_excel('/home/safwan/Documents/projects/python/Data Analysis/pandas/data/stock_data.xlsx',converters={
    'people': people_cell_convert,
    'price': price_cell_convert
})
print(df)

# Write to Excel
df.to_excel('data/new_data.xlsx', sheet_name='stocks')

df.to_excel('data/new_data.xlsx', sheet_name='stocks',startrow=1,startcol=2)

# Remove index
df.to_excel('data/new_data.xlsx', sheet_name='stocks', index=False)



# Write two dataframes to two separate sheets in excel

df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('stock_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name='stocks')
    df_weather.to_excel(writer, sheet_name='weather')
