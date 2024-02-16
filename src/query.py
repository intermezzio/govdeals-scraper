from selenium.webdriver.common.by import By
from selenium import webdriver

import locale
import requests

import constants as c

driver = webdriver.Firefox()
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def query():
    """
    """
    params = {
        "isAdvSearch": 1,
        "whichForm": "item",
        "category": 56, # watches
    }
    url = c.GOVDEALS_SEARCH_URL + "?" + "&".join(f"{k}={v}" for k,v in params.items())
    driver.get(url)

def process_search():
    """
    """
    cards = driver.find_elements(By.CSS_SELECTOR, "#grid div.card")
    for i, card in enumerate(cards):
        print(f"Entry {i+1}")
        get_card(card)

def get_card(card) -> dict[str,(str|int)]:
    """
    """
    title = card.find_element(By.CSS_SELECTOR, "p.card-title a").get_attribute("title")
    location = card.find_element(By.CSS_SELECTOR, "p[name=\"pAssetLocation\"]").get_attribute("title")
    current_bid = card.find_element(By.CSS_SELECTOR, "p[name=\"pAssetCurrentBid\"]").get_attribute("title")
    print(f"{title}\n\t{location}\n\t${current_bid}")
    return {
        "title": title,
        "location": location,
        "current_bid": current_bid,
    }
    


if __name__ == "__main__":
    query()
    process_search()