import requests

class CardService:
  base_url = 'https://api.scryfall.com/cards'

  def search_cards(name):
    # url = base_url + '/cards/search'
    url = 'https://api.scryfall.com/cards/named?'
    params = {'fuzzy': name}
    response = requests.get(url, params=params)

    if response.status_code == 200:
      return [response.json()]
    else:
      return []