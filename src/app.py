import alphavantage as api

def main():

    with open("config.json") as f:
        config = json.load(json_file)

    key = config["key"]
    symbol = input("Symbol: ")

    quote, overview = api.get_data(key, symbol)
    dict = generate_dict(quote, overview)


def get_data(key, symbol):
    """
    Gets following Data:
    - Global Quote
    - Company Overview
    """

    args = {"symbol": symbol, "key": key}

    quote = api.get_as_json("GLOBAL_QUOTE", args)
    print("Got Global Quote")
    overview = api.get_as_json("OVERVIEW", args)
    print("Got Overview")

    return quote, overview

def generate_dict(quote, overview):

    # 5 Year Average Dividend Yield
    # Forward Annual Dividend Rate
    # Frequency
    # DRIP Eligible
    # BNS Three Year Dividend Growth
    # Cash Flow => Request?

    dict = {}

    # Overview
    # ========
    # Sector
    # Beta
    # Market Cap
    # Book Value Per Share
    # Dividend Per Share
    # Dividend Yield
    # Dividend Pay Date
    # Ex-Dividend Date
    # P/E Ratio
    # Currency

    dict["sector"] = overview["Sector"]
    dict["beta"] = overview["Beta"]
    dict["market_cap"] = overview["MarketCapitalization"]
    dict["book_value_per_share"] = overview["BookValue"]
    dict["divident_per_share"] = overview["DividendPerShare"]
    dict["divident_yield"] = overview["DividendYield"]
    dict["divident_date"] = overview["DividendDate"]
    dict["ex_divident_date"] = overview["ExDividendDate"]
    dict["pe_ratio"] = overview["PERatio"]
    dict["currency"] = overview["Currency"]

    # GLOBAL QUOTE
    # =====
    # Stock Price

    dict["price"] = quote["05. price"]

if __name__ == '__main__':
    main()
