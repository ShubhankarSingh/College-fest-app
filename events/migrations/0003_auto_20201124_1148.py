# Generated by Django 3.0 on 2020-11-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201124_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]