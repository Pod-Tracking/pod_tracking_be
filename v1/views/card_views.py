from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..services.card_service import CardService
from ..serializers import CardSerializer
from ..models.card_model import Card

def populate_cards_view(request):
  query = request.GET.get('query')
  if query:
    cards_data = CardService.search_cards(query)
    for details in cards_data:
      card = Card.objects.create(
        name=details.get('name'),
        mana_cost=details.get('mana_cost'),
        cmc=details.get('cmc'),
        # color=details.get('color'),
        type_line=details.get('type_line'),
        rarity=details.get('rarity'),
        cmdr_legal=details.get('legalities'[12]),
        img=details.get('image_uris'[2]),
        purchase_uris=details.get('purchase_uris'[0])
      )
      card.save()
    return JsonResponse({'message': 'Card populated successfully'})
  else:
    return JsonResponse({'error': 'Query parameter is required'}, status=400)