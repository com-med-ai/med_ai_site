from django.db import models

class WhoAreWe(models.Model):
    name = models.TextField(max_length=32)
    text = models.TextField(max_length=4096)
    stylist_name = models.TextField(max_length = 32)

    def __str__(self) -> str:
        return f"{self.name}: {self.stylist_name}"

# Create your models here.
