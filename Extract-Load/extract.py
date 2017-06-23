import datetime as dt
import pandas as pd
from yahoo_finance import Share
from stocks import stocks_list

# The "extract" phase loops through stocks from a list stored in stocks.py
# daily and stores it in a Pandas dataframe

print("Extracting stock data from Yahoo Finance for the following stocks:")
print(stocks_list)
print("Extracting...")

df = pd.DataFrame(columns=["stock", "open", "high", "low", "close",
                           "volume", "date"])

i = 1
for item in stocks_list:
    stock = Share(item)
    df.loc[i] = [
        item,
        stock.get_open(),
        stock.get_days_high(),
        stock.get_days_low(),
        stock.get_prev_close(),
        stock.get_volume(),
        dt.date.today()
    ]
    i += 1

print("Returning generated DataFrame:")
print(df)

# The "load" phase takes the formatted dataframe and loads it into a Postgresql
# database where they will be available for analysis
