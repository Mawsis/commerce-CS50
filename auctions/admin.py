from django.contrib import admin

from .models import AuctionListing,Category 
# Register your models here.

admin.site.register(Category)
admin.site.register(AuctionListing)