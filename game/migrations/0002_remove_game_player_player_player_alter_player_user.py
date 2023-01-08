# Generated by Django 4.1.4 on 2023-01-07 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
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
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
    ]