import sys
from datetime import datetime, timedelta
import numpy
from binance.client import Client
import talib
from talib import RSI, MA_Type
import matplotlib.pyplot as plt
import csv

# --- Configuration & Hyperparameters ---
RSI_PERIOD = 6
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 20
SMA_PERIOD = 20

# Data storage lists
highs, lows, closes, times, counters, volumes, opens = [], [], [], [], [], [], []
boughtCloses, boughtTimes = [], []
soldCloses, soldTimes = [], []

# API Credentials (Replace with environment variables for security)
api_key = "****"
api_secret = "****"

# Backtesting starting parameters
startingMoney = 1000
money = startingMoney
status = False  # False = Looking to Buy, True = Currently Holding Position

# Initialize Binance Client
client = Client(api_key, api_secret)

# --- Data Acquisition ---
# Fetches 1-minute candlestick data for the last 30 days
candles = client.get_historical_klines("BTCTUSD", Client.KLINE_INTERVAL_1MINUTE, "30 days ago")

count = 0
for candlestick in candles:
    # Binance K-line indices: 1=Open, 2=High, 3=Low, 4=Close, 5=Volume, 6=CloseTime
    opens.append(round(float(candlestick[1])))
    highs.append(round(float(candlestick[2])))
    lows.append(round(float(candlestick[3])))
    closes.append(round(float(candlestick[4])))
    volumes.append(candlestick[5])
    # Convert MS timestamp to readable datetime
    times.append(datetime.fromtimestamp((candlestick[6]/1000)))
    count += 1
    counters.append(count)

# --- Indicator Calculation ---
# Convert lists to NumPy arrays for TA-Lib processing (Float64)
np_closes = numpy.array(closes, dtype='f8')
np_highs = numpy.array(highs, dtype='f8')
np_lows = numpy.array(lows, dtype='f8')
np_opens = numpy.array(opens, dtype='f8')
np_volumes = numpy.array(volumes, dtype='f8')

# Technical Indicators
sma = talib.SMA(np_closes, timeperiod=SMA_PERIOD)
rsi = talib.RSI(np_closes, RSI_PERIOD)
momentum = talib.MOM(np_closes, timeperiod=10)
obv = talib.OBV(np_closes, np_volumes)
OBV_momentum = talib.MOM(obv, timeperiod=10)
SMA_momentum = talib.MOM(sma, timeperiod=10)
macd, signal, hist = talib.MACD(np_closes)

# --- CSV Export ---
# Log technical data to CSV for external analysis
with open('test.csv', mode='w', newline='') as csvfile:
    fieldnames = ['open', 'high', 'low', 'close', 'volume', 'sma', 'rsi', 'momentum']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(len(np_closes)):
        writer.writerow({
            "open": np_opens[i],
            "high": np_highs[i],
            "low": np_lows[i],
            "close": np_closes[i],
            "volume": np_volumes[i],
            "sma": sma[i],
            "rsi": rsi[i],
            "momentum": momentum[i]
        })

# --- Backtesting Loop ---
boughtPrice = 0
shares = 0
timesBought = 0
timesSold = 0
count = 0

for close in np_closes:
    # 1. CHECK BUY CONDITION
    # Condition: RSI is oversold (<20) AND current price is below the 20-period SMA
    if not status and rsi[count] < RSI_OVERSOLD and np_closes[count] < sma[count]:
        boughtPrice = np_closes[count]
        shares = money / np_closes[count]  # "Buy" using all available capital
        status = True
        timesBought += 1
        boughtCloses.append(boughtPrice)
        boughtTimes.append(times[count])
        
        print(f"Bought: RSI={rsi[count]:.2f} | Price={np_closes[count]} | Time={times[count]}")

    # 2. CHECK SELL CONDITION
    # Condition A: Price is above SMA AND price has gained > 0.1% (Profit)
    # Condition B: Price is below bought price (Stop Loss/Exit on weakness)
    elif status:
        take_profit = np_closes[count] > boughtPrice + (boughtPrice * 0.001) and np_closes[count] > sma[count]
        stop_loss = np_closes[count] < boughtPrice
        
        if take_profit or stop_loss:
            money = shares * np_closes[count]  # Convert shares back to currency
            status = False
            timesSold += 1
            soldCloses.append(np_closes[count])
            soldTimes.append(times[count])
            
            print(f"Sold: RSI={rsi[count]:.2f} | Price={np_closes[count]} | Time={times[count]}")
            print(f"Current Balance: {money:.2f}\n")

    count += 1

# --- Final Results Calculation ---
print("-" * 30)
print(f"Resulting Money: {money:.2f}")
print(f"Starting Money: {startingMoney}")
percentage = ((money - startingMoney) / startingMoney) * 100
print(f"Total Gain/Loss: {percentage:.2f}%")
print(f"Trades: {timesBought} buys, {timesSold} sells")

# Display the plot
plt.grid()
plt.show()
