import datetime

from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.files import FileField, ImageField
from django.db.models.fields.related import ForeignKey, OneToOneField
from home.models import User



class Activities(models.Model):
    head = models.TextField(max_length=128, verbose_name='Etkinlik Adı')
    text = models.TextField(max_length=4096, verbose_name='Duyuru Metni')
    banner = ImageField(verbose_name='Afiş')
    doing_date = DateTimeField()
    #coordinator = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<{self.doing_date}>{self.head}"

    def is_public(self):
        now = datetime.now()
        return self.doing_date - datetime.timedelta(days=15) <= now <= self.doing_date

# Create your models here.
