from django.db import models

class WhoAreWe(models.Model):
    name = models.TextField(max_length=16)
    text = models.TextField(max_length=4096)

# Create your models here.
