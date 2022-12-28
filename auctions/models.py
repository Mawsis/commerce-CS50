from django.contrib.auth.models import AbstractUser
from django.db import models




class Category(models.Model):
    category = models.CharField(max_length=64)
    def __str__(self):
        return self.category

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300   )
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


class User(AbstractUser):
    watchlist = models.ManyToManyField(AuctionListing,blank=True,related_name="watchlisted")
    def isInWatchlist(self,title):
        listing = AuctionListing.objects.get(title=title)
        if listing in self.watchlist.all():
            return True
        else: return False
#class Bid(models.Model):
#    pass

#class Comment(models.Model):
#    pass
