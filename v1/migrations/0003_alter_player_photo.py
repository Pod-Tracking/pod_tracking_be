# Generated by Django 5.0.2 on 2024-02-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
