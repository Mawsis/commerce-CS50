from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Category,AuctionListing,Bid,Comment


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
        image = request.FILES['image']
        category = request.POST['category']
        category = Category.objects.get(category=category)
        auction = AuctionListing(seller=request.user,title=title,description=description,startingBid=startingBid,image=image,category=category)
        auction.save()
        return HttpResponseRedirect(reverse("index"))

def listing(request,name):
    listing = AuctionListing.objects.get(title=name)
    
    return render(request, "auctions/listing.html",{
        "listing":listing
    })

def watchlist(request,listing_id):
    if request.method == "POST":
        user = request.user
        listing = AuctionListing.objects.get(pk = int(listing_id))
        if listing in user.watchlist.all():
            user.watchlist.remove(listing)
        else:
            user.watchlist.add(listing)
            user.save()

        return HttpResponseRedirect(reverse("index"))
    
def bid(request,listing_id):
    if request.method == 'POST':
        amount = request.POST["amount"]
        listing = AuctionListing.objects.get(pk = int(listing_id))
        listing.price = amount
        listing.save()
        bid = Bid(bidder=request.user,listing=listing,amount=amount)
        bid.save()
        return HttpResponseRedirect(reverse("index"))
    
def close(request,listing_id):
    if request.method == 'POST':
        listing = AuctionListing.objects.get(pk = int(listing_id))
        bid = Bid.objects.get(amount=listing.price)
        listing.winner = bid.bidder
        bid.save()
        listing.save()
        return render(request, "auctions/listing.html",{
        "listing":listing
    })


def comment(request,listing_id):
    if request.method =='POST':
        comment = Comment(commenter=request.user,commented=AuctionListing.objects.get(pk=int(listing_id)),content=request.POST["content"])
        comment.save()
        return HttpResponseRedirect(reverse("index"))