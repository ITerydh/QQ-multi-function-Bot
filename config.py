import json
import random


def getToken():

    # Open the JSON configuration file
    with open("config.json", "r") as f:
        # Parse the JSON data
        configs = json.load(f)

    # Get the list of tokens from the JSON object
    key = configs["openai_key"]
    aid = configs["app_id"]
    asc = configs["app_secret"]
    gdkey = configs["gaode_key"]

    return key, aid, asc, gdkey


if __name__ == "__main__":

    key, aid, asc = getToken()
    print(key)
    print(aid)
    print(asc)
