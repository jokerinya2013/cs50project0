# Generated by Django 3.1.4 on 2020-12-15 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20201215_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at', 'id']},
        ),
    ]
