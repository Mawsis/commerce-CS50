# Generated by Django 4.1.4 on 2023-01-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_alter_auctionlisting_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
