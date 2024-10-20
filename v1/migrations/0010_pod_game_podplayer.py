# Generated by Django 5.0.2 on 2024-02-28 04:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0009_rename_losses_deck_total_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_log', models.TextField(default='', max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('decks', models.ManyToManyField(to='v1.deck')),
                ('loser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='all_games', to='v1.deck')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_games', to='v1.deck')),
                ('pod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.pod')),
            ],
        ),
        migrations.CreateModel(
            name='PodPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_win_perc', models.FloatField()),
                ('total_wins', models.IntegerField(default=0)),
                ('total_games', models.IntegerField(default=0)),
                ('total_kills', models.IntegerField(default=0)),
                ('kil_avg', models.IntegerField(default=0)),
                ('games_as_arch', models.IntegerField(default=0)),
                ('wins_as_arch', models.IntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='v1.player')),
                ('pod', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='v1.pod')),
            ],
        ),
    ]
