# 📈 Financial News Sentiment & Stock Trend Analysis
> **Project for Nova Financial Solutions** > An integrated pipeline to quantify market sentiment and correlate it with technical stock indicators.

---

## 📖 Project Overview
This project explores the relationship between financial news headlines and stock market movements. By using Natural Language Processing (NLP) to analyze sentiment from thousands of articles, we aim to discover if "market mood" can serve as a predictive indicator for price trends and volatility.

### ✨ Key Features
* **Sentiment Engine**: Dual-scoring using VADER and TextBlob to evaluate headline tone.
* **Technical Analysis**: Automated calculation of SMA, RSI, and MACD using `TA-Lib`.
* **Data Integration**: Seamless alignment of timezone-aware news data with historical price data.
* **Correlation Modeling**: Statistical analysis to identify stocks most sensitive to news flow.

---

## 🛠️ Tech Stack
* **Language**: Python 3.9+
* **Data Handling**: Pandas, NumPy
* **NLP**: NLTK (VADER), TextBlob
* **Finance**: yfinance, TA-Lib
* **Visualization**: Matplotlib, Seaborn, mplfinance

---

## 📊 Methodology
### 1. Sentiment Analysis
We process headlines to generate a **Compound Score** (-1 to 1). 
* **VADER** is used for financial nuance.
* **TextBlob** provides subjectivity context.

### 2. Quantitative Indicators
We calculate momentum and trend indicators to contextualize sentiment:
* **SMA (20)**: To identify the primary trend.
* **RSI (14)**: To identify overbought/oversold conditions (e.g., RSI > 70).

### 3. Correlation
We align daily sentiment averages with stock log returns to calculate the **Pearson Correlation Coefficient**.

---

## 🚀 Getting Started

### Prerequisites
* Python installed
* TA-Lib dependencies (requires C++ build tools on Windows)

### Installation
1. Clone the repo:
   ```bash
   git clone [https://github.com/your-username/financial-news-sentiment.git](https://github.com/your-username/financial-news-sentiment.git)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the analysis:
   ```bash
   python src/main.py 
