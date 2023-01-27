from django.contrib import admin

from .models import Bid,AuctionListing,User,Category 
# Register your models here.

admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(User)
admin.site.register(Bid)