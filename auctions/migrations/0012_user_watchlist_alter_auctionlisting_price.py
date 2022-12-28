# Generated by Django 4.1.4 on 2022-12-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auctionlisting_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlisted', to='auctions.auctionlisting'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]