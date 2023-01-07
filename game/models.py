from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=255)
    rounds_amount = models.PositiveIntegerField(null=False)
    type = models.CharField(max_length=25, default='Classic')
    is_finished = models.BooleanField(default=False)
    # first_place = models.PositiveIntegerField()
    # second_place = models.PositiveIntegerField()
    # third_place = models.PositiveIntegerField()


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='player')
    last_game = models.ForeignKey(Game, on_delete=models.PROTECT, related_name='game', null=True, blank=True)
    games_played = models.PositiveIntegerField(default=0)
    max_points = models.PositiveIntegerField(default=0)
