import pandas as pd

def load_data(filepath):
    """
    Load the raw analyst ratings dataset.
    """
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df

def prepare_stock_df(df, price_col='price'):
    """
    Prepare stock price dataframe from the same CSV.
    Assumes 'date', 'stock', and a numeric 'price' column exist.
    """
    stock_df = df[['date', 'stock', price_col]].copy()
    stock_df = stock_df.rename(columns={price_col: 'Close'})
    stock_df.set_index('date', inplace=True)
    return stock_df

def align_dates(df):
    """
    Floor the datetime to day for easier alignment
    """
    df['date'] = df['date'].dt.floor('D')
    return df
