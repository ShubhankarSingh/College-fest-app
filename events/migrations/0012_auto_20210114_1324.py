# Generated by Django 2.2 on 2021-01-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20210112_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]