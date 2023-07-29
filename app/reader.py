import argparse
from ast import literal_eval
import os


import pandas as pd



def create_cardprices(path_to_data) -> pd.DataFrame:
    """
    Creating a DataFrame including the name of the card and the corresponding price 
    from the mtgjson dataset.
    """
    cards = pd.read_csv(os.path.join(path_to_data, "AllPrintingsCSVFiles/cards.csv"),
                        low_memory=False)

    cardinfo = cards[["name", "uuid", "setCode"]]

    prices = pd.read_json(os.path.join(path_to_data, "AllPrices.json"))

    prices["uuid"] = prices.index
    prices.reset_index(inplace=True)

    cardprices = pd.merge(left=cardinfo, right=prices, on="uuid")

    print(f"length of cardinfo: {len(cardinfo)}")
    print(f"length of prices: {len(prices)}")
    print(f"length of cardprices (merged df): {len(cardprices)}")

    cardprices.to_csv("data/cardprices.csv", index=False)
    
    return cardprices



def get_cardprice_name(cardname, cardprices):
    filtered_df = cardprices[cardprices["name"].isin([cardname])] 
    cardprices = pd.DataFrame.from_dict(literal_eval(filtered_df["name"]["data"])["paper"]["cardmarket"]['retail'])
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='cardprices',
            description='Creating a DataFrame with cardprices from mtgjson',
            epilog='Please enter the mtgjson directory path')
    parser.add_argument('data')
    args = parser.parse_args()

    create_cardprices(path_to_data=args.data)
