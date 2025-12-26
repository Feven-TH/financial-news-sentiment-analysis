import matplotlib.pyplot as plt

def plot_stock_with_indicators(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Close'], label='Close')
    if 'SMA_20' in df: plt.plot(df['SMA_20'], label='SMA 20')
    if 'SMA_50' in df: plt.plot(df['SMA_50'], label='SMA 50')
    plt.title("Stock Price with Moving Averages")
    plt.legend()
    plt.show()

def plot_sentiment(df):
    if 'vader_sentiment' in df:
        df['vader_sentiment'].hist(bins=30)
        plt.title("VADER Sentiment Distribution")
        plt.show()
    if 'textblob_sentiment' in df:
        df['textblob_sentiment'].hist(bins=30)
        plt.title("TextBlob Sentiment Distribution")
        plt.show()
