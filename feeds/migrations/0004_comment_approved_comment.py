# Generated by Django 3.1.1 on 2020-10-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20201028_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
