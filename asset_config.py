"""
Asset Configuration for QuantAgent Trading System

This file contains the default asset mappings for popular trading instruments.
Users can modify this file to customize the available assets in the web interface.

Format: "TICKER": "Display Name"
- TICKER: Yahoo Finance ticker symbol
- Display Name: Human-readable name shown in the UI

EXAMPLES OF HOW TO ADD CUSTOM ASSETS:
=====================================

1. Adding a stock:
   "IBM": "IBM Corp.",

2. Adding a cryptocurrency:
   "AVAX-USD": "Avalanche",

3. Adding a commodity:
   "ZC=F": "Corn Futures",

4. Adding an index:
   "^GSPC": "S&P 500 Index",

5. Adding a forex pair:
   "EURGBP=X": "EUR/GBP",

Simply add your entries to the DEFAULT_ASSETS dictionary below following the same format.
After editing this file, restart the web_interface.py server to see your changes.
"""

# Default assets available in the trading system
DEFAULT_ASSETS = {
    # Major Cryptocurrencies
    "BTC-USD": "Bitcoin",
    "ETH-USD": "Ethereum",
    "BNB-USD": "Binance Coin",
    "XRP-USD": "Ripple",
    "ADA-USD": "Cardano",
    "DOGE-USD": "Dogecoin",
    "SOL-USD": "Solana",

    # Precious Metals & Commodities
    "GC=F": "Gold Futures",
    "SI=F": "Silver Futures",
    "CL=F": "Crude Oil",
    "NG=F": "Natural Gas",
    "HG=F": "Copper",
    "PL=F": "Platinum",

    # Major US Tech Stocks (Top S&P 500)
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corp.",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com Inc.",
    "NVDA": "NVIDIA Corp.",
    "META": "Meta Platforms Inc.",
    "TSLA": "Tesla Inc.",
    "BRK-B": "Berkshire Hathaway",
    "JPM": "JPMorgan Chase",
    "V": "Visa Inc.",
    "JNJ": "Johnson & Johnson",
    "WMT": "Walmart Inc.",
    "PG": "Procter & Gamble",
    "MA": "Mastercard Inc.",
    "UNH": "UnitedHealth Group",
    "HD": "Home Depot",
    "DIS": "Walt Disney Co.",
    "BAC": "Bank of America",
    "XOM": "Exxon Mobil Corp.",
    "CVX": "Chevron Corp.",
    "KO": "Coca-Cola Co.",
    "PFE": "Pfizer Inc.",
    "NFLX": "Netflix Inc.",
    "CSCO": "Cisco Systems",
    "INTC": "Intel Corp.",
    "AMD": "Advanced Micro Devices",
    "PYPL": "PayPal Holdings",
    "ADBE": "Adobe Inc.",
    "CRM": "Salesforce Inc.",
    "ORCL": "Oracle Corp.",

    # Major European Stocks (Stoxx 50)
    "ASML.AS": "ASML Holding (Stoxx50)",
    "MC.PA": "LVMH (Stoxx50)",
    "OR.PA": "L'Oréal (Stoxx50)",
    "SAP.DE": "SAP SE (Stoxx50)",
    "SAN.PA": "Sanofi (Stoxx50)",
    "TTE.PA": "TotalEnergies (Stoxx50)",
    "SIE.DE": "Siemens AG (Stoxx50)",
    "AIR.PA": "Airbus SE (Stoxx50)",
    "DTE.DE": "Deutsche Telekom (Stoxx50)",
    "ALV.DE": "Allianz SE (Stoxx50)",
    "BNP.PA": "BNP Paribas (Stoxx50)",

    # ETFs and Indices
    "SPY": "SPDR S&P 500 ETF",
    "QQQ": "Invesco QQQ Trust",
    "DIA": "SPDR Dow Jones ETF",
    "IWM": "iShares Russell 2000",
    "VTI": "Vanguard Total Stock Market",
    "VOO": "Vanguard S&P 500",
    "VEA": "Vanguard FTSE Developed Markets",
    "VWO": "Vanguard FTSE Emerging Markets",

    # Major Forex Pairs (via futures/ETFs)
    "EURUSD=X": "EUR/USD",
    "GBPUSD=X": "GBP/USD",
    "USDJPY=X": "USD/JPY",
    "AUDUSD=X": "AUD/USD",
    "USDCAD=X": "USD/CAD",
    "USDCHF=X": "USD/CHF",
}

# Yahoo Finance symbol mapping for special cases (XAU/USD, XAU/EUR, etc.)
# These mappings allow users to use common trading symbols that map to Yahoo Finance equivalents
SYMBOL_MAPPING = {
    "XAU/USD": "GC=F",      # Gold Futures (XAU/USD proxy)
    "XAUUSD": "GC=F",       # Alternative format
    "XAU/EUR": "GOLDEUR=X", # Gold in EUR
    "XAUEUR": "GOLDEUR=X",  # Alternative format
}

# Yahoo Finance interval mapping for timeframes
INTERVAL_MAPPING = {
    "1m": "1m",
    "5m": "5m",
    "15m": "15m",
    "30m": "30m",
    "1h": "1h",
    "4h": "4h",
    "1d": "1d",
    "1w": "1wk",
    "1mo": "1mo",
}
