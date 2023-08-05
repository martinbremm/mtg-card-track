import requests


def get_card_image(card_name, set_name):
    url = "https://api.scryfall.com/cards/named?fuzzy={}&set={}".format(
        card_name, set_name
    )
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()["image_uris"]
