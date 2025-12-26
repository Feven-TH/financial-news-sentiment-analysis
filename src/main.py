import pandas as pd
import yfinance as yf
from src.data_prep import load_data, align_dates
from src.sentiment import add_sentiment_scores
from src.indicators import add_technical_indicators

def run_analysis():
    # 1. Load News Data
    print("--- Loading News Data ---")
    news_df = load_data("data/raw_analyst_ratings.csv")
    news_df = align_dates(news_df)
    
    # FIX: Use .copy() to avoid SettingWithCopyWarning
    news_sample = news_df[news_df['date'] >= '2020-01-01'].copy()
    
    # 2. Sentiment Analysis
    print("--- Running Sentiment Analysis ---")
    news_sample = add_sentiment_scores(news_sample)
    
    # 3. Fetch Stock Data
    print("--- Fetching Stock Price Data ---")
    tickers = news_sample['stock'].unique().tolist()
    price_data = yf.download(tickers, start="2020-01-01", end="2024-01-01")

    # FIX: TypeError (Cannot join tz-naive with tz-aware)
    # Force the stock index to be timezone-naive to match the news data
    if price_data.index.tz is not None:
        price_data.index = price_data.index.tz_localize(None)

    # 4. Quantitative Analysis (Task 2)
    print("--- Calculating Technical Indicators ---")
    indicator_results = {}
    for ticker in tickers:
        try:
            # Extract specific ticker data (Open, High, Low, Close, Volume)
            ticker_df = price_data.xs(ticker, axis=1, level=1).copy()
            if ticker_df['Close'].dropna().empty:
                continue
                
            # Add indicators from your src.indicators
            ticker_df = add_technical_indicators(ticker_df)
            indicator_results[ticker] = ticker_df
        except Exception as e:
            print(f"Could not process indicators for {ticker}: {e}")

    # 5. Correlation Analysis (Task 3)
    print("--- Calculating Correlation ---")
    # Use 'Close' for returns
    # Update the correlation logic slightly to be more robust
    stock_returns = price_data['Close'].pct_change(fill_method=None).dropna() 
    if stock_returns.index.tz is not None:
        stock_returns.index = stock_returns.index.tz_localize(None)

    # Aggregate news sentiment by date and stock
    daily_sent = news_sample.groupby(['date', 'stock'])['vader_sentiment'].mean().unstack()
    
    # Ensure the sentiment index is datetime and naive
    daily_sent.index = pd.to_datetime(daily_sent.index).tz_localize(None)

    # Align dates (intersection of news days and trading days)
    common_dates = daily_sentiment_index = daily_sent.index.intersection(stock_returns.index)
    
    # Calculate correlation per ticker
    # We use .loc[common_dates] to ensure we aren't comparing weekend news to non-existent prices
    correlation = daily_sent.loc[common_dates].corrwith(stock_returns.loc[common_dates])

    # 6. Final Outputs
    print("\n" + "="*40)
    print("CORRELATION RESULTS (Top 5 Stocks)")
    print("="*40)
    print(correlation.dropna().sort_values(ascending=False).head())

    # Example of indicator check for Task 2
    valid_tickers = list(indicator_results.keys())
    if valid_tickers:
        print(f"\nIndicators for {valid_tickers[0]}:")
        print(indicator_results[valid_tickers[0]][['Close', 'SMA_20', 'RSI_14']].tail())

if __name__ == "__main__":
    run_analysis()