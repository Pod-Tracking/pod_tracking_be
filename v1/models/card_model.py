from django.db import models

class Card(models.Model):
  name = models.CharField(max_length=255)
  mana_cost = models.CharField(max_length=50)
  cmc = models.IntegerField(default=0)
  colors = models.CharField(max_length=100, default='')
  type_line = models.CharField(max_length=255)
  # set = models.CharField(max_length=255) # For a future iteration
  rarity = models.CharField(max_length=50)
  cmdr_legal = models.CharField(max_length=50)
  img = models.URLField()
  purchase_uris = models.URLField()

  def __str__(self):
    return self.name