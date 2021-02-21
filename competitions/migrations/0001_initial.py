# Generated by Django 2.2 on 2020-12-09 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=200)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='default-image.png', null=True, upload_to='images')),
                ('description', models.TextField(default='', max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['time'],
                'verbose_name_plural': 'competitions',
            },
        ),
        migrations.CreateModel(
            name='CompetitionRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('competition', 'user')},
                'verbose_name_plural': 'Attendes for competitions',
            },
        ),
    ]