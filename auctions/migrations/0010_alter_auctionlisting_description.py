# Generated by Django 4.1.4 on 2022-12-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_auctionlisting_currentprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]