from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name