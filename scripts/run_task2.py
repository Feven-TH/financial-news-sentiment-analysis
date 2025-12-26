from src.data_prep import load_data, prepare_stock_df, align_dates
from src.sentiment import add_sentiment_scores
from src.indicators import add_technical_indicators

if __name__ == "__main__":
    df = load_data("data/raw_analyst_ratings.csv")
    stock_df = prepare_stock_df(df, price_col='price')  
    df = align_dates(df)
    df = add_sentiment_scores(df, column='headline') 
    stock_df = add_technical_indicators(stock_df)

    print(df.head())
    print(stock_df.head())
