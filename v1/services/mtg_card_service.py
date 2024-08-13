import requests

# Not currently in use!
class CardService:
    def search_cards(search_query):
        url = 'https://api.magicthegathering.io/v1/cards?'
        params = {'name': search_query}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return [response.json()]
        else:
            return []