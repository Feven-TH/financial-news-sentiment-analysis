import unittest
from src.sentiment import vader_sentiment, textblob_sentiment

class TestSentiment(unittest.TestCase):

    def test_vader(self):
        text = "Stock prices are soaring!"
        score = vader_sentiment(text)
        self.assertTrue(-1 <= score <= 1)

    def test_textblob(self):
        text = "Stock prices are terrible."
        score = textblob_sentiment(text)
        self.assertTrue(-1 <= score <= 1)

if __name__ == "__main__":
    unittest.main()
