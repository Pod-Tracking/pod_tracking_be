# Generated by Django 5.0.2 on 2024-03-04 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0012_remove_game_loser_game_losers_alter_game_game_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='losers',
        ),
        migrations.AlterField(
            model_name='game',
            name='decks',
            field=models.ManyToManyField(related_name='all_games', to='v1.deck'),
        ),
    ]
