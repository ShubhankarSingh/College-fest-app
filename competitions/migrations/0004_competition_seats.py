# Generated by Django 2.2 on 2021-01-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_competition_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='seats',
            field=models.IntegerField(default=50),
        ),
    ]
