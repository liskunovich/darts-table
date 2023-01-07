# Generated by Django 4.1.4 on 2023-01-07 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_remove_player_player_game_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='player',
        ),
        migrations.AddField(
            model_name='player',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='player_of_the_game', to='game.game'),
            preserve_default=False,
        ),
    ]
