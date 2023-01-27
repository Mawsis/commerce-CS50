# Generated by Django 4.1.4 on 2023-01-26 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_user_watchlist_alter_auctionlisting_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.auctionlisting')),
            ],
        ),
    ]
