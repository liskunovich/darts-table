from django.contrib import admin
from game.models import Player, Game


# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [Player.name for Player in Player._meta.fields]
    fields = ['user', 'last_game', 'games_played', 'max_points']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = [Game.name for Game in Game._meta.fields]
    fields = ['name', 'rounds_amount', 'type', 'is_finished']
