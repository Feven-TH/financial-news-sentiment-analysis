import pandas as pd
import ta  # using the Python 'ta' package instead of TA-Lib

def add_technical_indicators(df):
    """
    Adds simple technical indicators: SMA, RSI, MACD
    Assumes df has 'Close' column
    """
    df = df.sort_index()  # ensure date order

    # Moving averages
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # RSI
    df['RSI_14'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()

    # MACD
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()

    return df
