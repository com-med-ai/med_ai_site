from django.db import models
from home.models import User


class Team(models.Model):
    team_name = models.TextField(max_length=64)
    description = models.TextField(max_length=4096)
    stylist_name = models.TextField(max_length=64)
    team_leader = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.stylist_name}: {self.team_name}"

# Create your models here.
