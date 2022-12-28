from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Category,AuctionListing


def index(request):
    listings = AuctionListing.objects.all()
    return render(request, "auctions/index.html",{
        "listings":listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def createListing(request):
    if request.method == "GET":
        return render(request,"auctions/createListing.html",{
            "categories":Category.objects.all()
        })
    else:
        title = request.POST['title']
        description = request.POST['description']
        startingBid = request.POST['startingBid']
        image = request.POST['image']
        category = request.POST['category']
        category = Category.objects.get(category=category)
        auction = AuctionListing(title=title,description=description,startingBid=startingBid,image=image,category=category)
        auction.save()
        return HttpResponseRedirect(reverse("index"))

def listing(request,name):
    listing = AuctionListing.objects.get(title=name)
    
    return render(request, "auctions/listing.html",{
        "listing":listing
    })

def watchlist(request):
    if request.method == "POST":
        user = User.objects.get(request.POST['user'])
        auctionListing =AuctionListing.objects.get(request.POST['listing'])
        for item in user.watchlist.all():
            if item == auctionListing:
                user.watchlist.remove(auctionListing)
            else:
              user.watchlist.add(auctionListing)  
        
        return render(request, HttpResponseRedirect(reverse("index")))