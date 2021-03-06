# Generated by Django 2.2 on 2020-12-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(blank=True, default='default-image.png', null=True, upload_to='images')),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'teams',
            },
        ),
    ]
