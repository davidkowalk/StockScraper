import alphavantage as api
from math import floor
import json

def main():

    with open("config.json") as f:
        config = json.load(f)

    key = config["key"]
    #symbol = input("Symbol: ")

    keyword = input("Search: ")
    args = {"keywords": keyword, "apikey": key}

    matches = api.get_as_json("SYMBOL_SEARCH", args)["bestMatches"]
    #print(json.dumps(matches, indent=4))

    for i in range(len(matches)):
        print(f"""{i}) {matches[i]["2. name"]} ({round(float(matches[i]["9. matchScore"])*10000)/100}%)
        - Symbol:\t{matches[i]["1. symbol"]}
        - Region:\t{matches[i]["4. region"]}
        - Currency:\t{matches[i]["8. currency"]}
        """)

    selection = None

    while type(selection) != int:
        try:
            selection = int(input("Select: "))

            if selection >= len(matches):
                print("Out of bounds! Please Select one of the above!\n")
                selection = None
        except:
            print("Please enter a number!\n")

    selected_stock = matches[selection]
    symbol = selected_stock["1. symbol"]

    quote, overview = load_data(key, symbol)

    #print(json.dumps(quote, indent = 4))

    dict = generate_dict(quote, overview)

    print(json.dumps(dict, indent=4))

def load_data(key, symbol):
    """
    Gets following Data:
    - Global Quote
    - Company Overview
    """

    args = {"symbol": symbol, "apikey": key}

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
    try:
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
    except Exception as e:
        print("ERROR IN DICT!")
        print(e)
        print(json.dumps(overview, indent=4))

    # GLOBAL QUOTE
    # =====
    # Stock Price
    try:
        quote = quote["Global Quote"]
        dict["price"] = quote["05. price"]
        dict["n_shares"] = floor(10000/float(dict["price"]))
        
    except Exception as e:
        print("ERROR IN DICT!")
        print(e)
        print(json.dumps(quote, indent=4))


    return dict

if __name__ == '__main__':
    main()
