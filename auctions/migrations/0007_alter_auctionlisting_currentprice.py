# Generated by Django 4.1.4 on 2022-12-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auctionlisting_currentprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='currentPrice',
            field=models.IntegerField(),
        ),
    ]
