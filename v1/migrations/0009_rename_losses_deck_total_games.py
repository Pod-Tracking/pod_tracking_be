# Generated by Django 5.0.2 on 2024-02-28 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0008_rename_updated_at_deck_updated_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='losses',
            new_name='total_games',
        ),
    ]