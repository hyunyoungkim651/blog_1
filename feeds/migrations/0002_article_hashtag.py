# Generated by Django 3.1.1 on 2020-10-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hashtag',
            field=models.ManyToManyField(to='feeds.HashTag'),
        ),
    ]
