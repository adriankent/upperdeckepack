import requests
import browser_cookie3
import tablib
from tqdm import tqdm

url = "https://www.upperdeckepack.com/api/Collection/ViewCards/"
search_filters = "o_u"
params = {"page": 1, "filters": search_filters}

ud_cookies = browser_cookie3.load(domain_name="www.upperdeckepack.com")
r = requests.get(url=url, cookies=ud_cookies, params=params)
card_data = r.json()
num_pages = card_data["Pages"] + 1
cur_page = 1
card_inventory = tablib.Dataset(
    headers=[
        "Card Set",
        "Card Number",
        "Card Player",
        "Card Team",
        "Quantity",
        "Front Photo",
        "Rear Photo",
        "Physical Card",
        "Big Hit",
    ]
)
for cur_page in tqdm(range(1, num_pages)):
    params = {"page": cur_page, "filters": search_filters}
    r = requests.get(url=url, cookies=ud_cookies, params=params)
    card_data = r.json()
    card_data_list = card_data["DisplayCards"]
    for card in card_data_list:
        card_info = card["CardTemplate"]
        card_is_physical = card_info["IsPhysical"]
        card_set = card_info["InsertName"]
        card_player = card_info["PlayerName"]
        card_number = card_info["CardNumber"]
        card_team = card_info["Team"]
        card_quantity = card_info["Owned"]
        card_photo_front = card_info["Image"]["Front"]
        card_photo_back = card_info["Image"]["Back"]
        card_big_hit = card_info["bigHit"]
        card_inventory.append(
            [
                card_set,
                card_number,
                card_player,
                card_team,
                card_quantity,
                card_photo_front,
                card_photo_back,
                card_is_physical,
                card_big_hit,
            ]
        )

    cur_page += 1
with open("epackexport.csv", "w", newline="") as f:
    f.write(card_inventory.export("csv"))
