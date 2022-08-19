import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import numpy as np
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

"""https://www.learndatasci.com/tutorials/python-finance-part-2-intro-quantitative-trading-strategies/"""


"""Dates we care about"""
start_date = '2019-03-14'
end_date = '2022-05-12'

stocks = ['AAPL', 'MSFT', '^GSPC']

"""Read data from yahoo"""
panel_data = pdr.DataReader(stocks, 'yahoo', start_date, end_date)

"""Save data to .csv"""
panel_data.to_csv('./data_folder/panel_data.csv')
# print("panel_data is", type(panel_data))
# print(panel_data.head(6))

"""collecting all the close values"""
close = panel_data['Close']

"""Getting all weekdays between start_date and end_date"""
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

"""How do we align the existing prices in adj_close with our new set of dates?
All we need to do is reindex close using all_weekdays as the new index"""
close = close.reindex(all_weekdays)
# print("close is a", type(close))
# print(close.head(6))

"""Reindexing will insert missing values (NaN) for the dates that were not present
in the original set. To cope with this, we can fill the missing by replacing them
with the latest available price for each instrument."""
close = close.fillna(method='ffill')
close.to_csv('./data_folder/close.csv')
print("close(reindexed) is", type(close))
print(close.head(6))

info_close = close.describe()  # Seem to work on any dataframe, uses pandas,gives lots of values, mean, std, 75% etc


def explane_describe_function():
    print("\n below follows 4 explanations and its values: \n")
    print("\n"
          "info_close:\n",
          info_close)
    print("\n"
          "type(info_close):\n",
          type(info_close))
    std_close = info_close.iloc[2]
    print("\n"
          "std_close:\n",
          std_close)
    print("\n type(std_close):\n", type(std_close))


explane_describe_function()


"""Get the MSFT timeseries. This now returns a Pandas Series object indexed by date."""
msft = close.loc[:, 'MSFT']
aapl = close.loc[:, 'AAPL']
gspc = close.loc[:, '^GSPC']
print("\n msft: \n", msft)
print("\n msft.index: \n", msft.index)

"""Calculate the 20 and 100 days moving averages of the closing prices"""
short_rolling_msft = msft.rolling(window=20).mean()
long_rolling_msft = msft.rolling(window=100).mean()
print("\n short_rolling_msft: \n", short_rolling_msft)

short_rolling_aapl = aapl.rolling(window=20).mean()
long_rolling_aapl = aapl.rolling(window=100).mean()

short_rolling_gspc = gspc.rolling(window=20).mean()
long_rolling_gspc = gspc.rolling(window=100).mean()

"""Plot everything by leveraging the very powerful matplotlib package"""


def plotting_rolling_and_actual():
    fig, ax = plt.subplots(figsize=(16, 9))

    ax.plot(msft.index, msft, label='MSFT')
    ax.plot(short_rolling_msft.index, short_rolling_msft, label='20 days rolling')
    ax.plot(long_rolling_msft.index, long_rolling_msft, label='100 days rolling')

    ax.plot(aapl.index, aapl, label='AAPL')
    ax.plot(short_rolling_aapl.index, short_rolling_aapl, label='20 days rolling AAPL')
    ax.plot(long_rolling_aapl.index, long_rolling_aapl, label='100 days rolling AAPL')

    # ax.plot(gspc.index, gspc, label='^GSPC')
    # ax.plot(short_rolling_gspc.index, short_rolling_gspc, label='20 days rolling ^GSPC')
    # ax.plot(long_rolling_gspc.index, long_rolling_gspc, label='100 days rolling ^GSPC')

    ax.set_xlabel('Date')
    ax.set_ylabel('Adjusted closing price ($)')
    ax.legend()
    plt.show()


plotting_rolling_and_actual()

"""Create a .pkl file"""
panel_data.to_pickle('./data_folder/panel_data.pkl')
data = pd.read_pickle('./data_folder/panel_data.pkl')
print("\n"
      "these 10 values below, are red from the .pkl file: \n \n",
      data.head(10))

# input('Press ENTER to exit')
# exit()

# testing 1,2
