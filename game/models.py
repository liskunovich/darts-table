from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    class GameType(models.IntegerChoices):
        CLS = 1, "CLASSIC",
        TEX = 2, "TEXAS"

    date = models.DateField(auto_now_add=True)
    rounds_amount = models.PositiveIntegerField(null=False)
    type = models.PositiveSmallIntegerField(
        choices=GameType.choices,
        default=GameType.CLS
    )
    is_finished = models.BooleanField(default=False)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='player')
    name = models.CharField(max_length=255, default='', null=False)
    surname = models.CharField(max_length=255, default='', null=False)
    last_game = models.ForeignKey(Game, on_delete=models.SET_NULL, related_name='game', null=True, blank=True)
    games_played = models.PositiveIntegerField(default=0)
    max_points = models.PositiveIntegerField(default=0)
