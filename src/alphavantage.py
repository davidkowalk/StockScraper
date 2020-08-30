import requests
import json

def get_as_json(function:str, args: dict, endpoint = "https://www.alphavantage.co/query?"):
    endpoint += f"function={function}"

    for arg in args:
        endpoint += f"&{arg}={args[arg]}"

    response = requests.get(endpoint)

    dic = json.loads(response.text)

    return dic
