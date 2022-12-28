from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)
    def __str__(self):
        return self.category

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300,blank=True)
    startingBid = models.IntegerField()
    image = models.ImageField(blank=True)
    category = models.ForeignKey( Category , on_delete=models.CASCADE , related_name="all_items")
    def __str__(self):
        return self.title

#class Bid(models.Model):
#    pass

#class Comment(models.Model):
#    pass
