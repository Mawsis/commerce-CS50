# Generated by Django 4.1.4 on 2022-12-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctionlisting_currentprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='currentPrice',
            field=models.IntegerField(blank=True),
        ),
    ]
