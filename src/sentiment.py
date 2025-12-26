from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Initialize the analyzer ONCE at the top of the script
# This stays in memory and is reused
sia = SentimentIntensityAnalyzer()

def vader_sentiment(text):
    # Just use the global 'sia' instead of creating a new one
    return sia.polarity_scores(str(text))['compound']

def textblob_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

def add_sentiment_scores(df, column='headline'):
    """
    Adds sentiment scores to a dataframe.
    """
    # Using .map or .apply is now much faster because 'sia' is ready
    df['vader_sentiment'] = df[column].apply(vader_sentiment)
    df['textblob_sentiment'] = df[column].apply(textblob_sentiment)
    return df