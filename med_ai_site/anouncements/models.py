from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

"""
class Anouncements(models.Model):
    head = models.TextField(max_length=128)
    text = models.TextField(max_length=4096)
    publication_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"<{self.publication_date}> {self.head}"

class AnonuncemntPhotos(models.Model):
    image = ImageField(verbose_name='Resim')
    anouncement = ForeignKey(Anouncements, on_delete=models.CASCADE)"""

# Create your models here.
