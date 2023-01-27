from django.contrib.auth.models import AbstractUser
from django.db import models




class Category(models.Model):
    category = models.CharField(max_length=64)
    def __str__(self):
        return self.category

class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    watchlisted = models.ManyToManyField(User,blank=True,related_name="watchlist")
    seller = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,related_name="listings")
    winner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="winnings")
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    startingBid = models.IntegerField()
    image = models.ImageField(blank=True)
    category = models.ForeignKey( Category , on_delete=models.CASCADE , related_name="all_items")
    price = models.IntegerField(blank=True)
    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.startingBid
        super(AuctionListing, self).save(*args, **kwargs)
    def __str__(self):
        return self.title



    

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE,related_name="bids")
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE,related_name="bids")
    amount = models.IntegerField()


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,related_name="comments")
    commented = models.ForeignKey(AuctionListing,on_delete=models.CASCADE,related_name="comments")
    content = models.CharField(max_length=300)