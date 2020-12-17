# Generated by Django 3.1.4 on 2020-12-12 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_category_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='creater',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
    ]
