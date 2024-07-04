import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns


tickers = yf.Tickers("BRK-B MC.PA RMS.PA")

# print(tickers.history(period="1mo"))


# Fetch historical stock data
def fetch_data(stocks, start_date, end_date):
    """
    yf conveniently returns a pandas dataframe
    """
    data = yf.download(stocks, start=start_date, end=end_date)["Adj Close"]
    return data


# Calculate portfolio performance metrics
def calculate_performance(data, weights):
    daily_returns = data.pct_change().dropna()
    portfolio_returns = daily_returns.dot(weights)
    avg_returns = portfolio_returns.mean() * 252
    portfolio_volatility = portfolio_returns.std() * np.sqrt(252)
    risk_free_rate = 0.005  # Example risk-free rate
    sharpe_ratio = (avg_returns - risk_free_rate) / portfolio_volatility
    return (
        daily_returns,
        avg_returns,
        portfolio_returns,
        portfolio_volatility,
        sharpe_ratio,
    )


# Visualization of portfolio performance
def visualize_performance(data, weights):
    daily_returns = data.pct_change().dropna()
    portfolio_returns = (daily_returns.dot(weights) + 1).cumprod()
    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_returns, label="Portfolio Cumulative Returns")
    plt.title("Portfolio Performance")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")
    plt.legend()
    plt.show()


# running the functions

# offensive portfolio
stocks = ["BRK-B", "MC.PA", "PYPL", "GOOG", "AMD"]
start_date = "2015-01-01"
end_date = "2023-12-31"
weights_offensive_pf = np.array([0.42, 0.25, 0.17, 0.11, 0.05])


data = fetch_data(stocks, start_date, end_date)
daily_returns, avg_returns, portfolio_returns, portfolio_volatility, sharpe_ratio = (
    calculate_performance(data, weights_offensive_pf)
)
print(f"Average Annual Return: {avg_returns:.2%}")
print(f"Annual Volatility: {portfolio_volatility:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
# visualize_performance(data, weights_offensive_pf)

print(daily_returns.corr())
sns.heatmap(daily_returns.corr())
plt.show()
