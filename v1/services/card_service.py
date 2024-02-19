import requests

class CardService:
  base_url = 'https://api.scryfall.com/cards'

  def search_cards(query):
    # url = base_url + '/cards/search'
    url = 'https://api.scryfall.com/cards/named?'
    params = {'fuzzy': query}
    response = requests.get(url, params=params)

    if response.status_code == 200:
      data = response.json()
      return data.get('data', [])
    else:
      return []