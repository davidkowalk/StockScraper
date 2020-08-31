import requests
import json

def get_as_json(function:str, args: dict, endpoint = "https://www.alphavantage.co/query?", debug=False):
    endpoint += f"function={function}"

    for arg in args:
        endpoint += f"&{arg}={args[arg]}"

    if debug:
        print(endpoint)

    response = requests.get(endpoint)

    dic = json.loads(response.text)

    return dic
