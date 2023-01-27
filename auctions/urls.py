from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.createListing, name="createListing"),
    path("listing/<str:name>",views.listing,name="listing"),
    path("watchlist/<str:listing_id>",views.watchlist,name="watchlist"),
    path("bid/<str:listing_id>",views.bid,name="bid"),
    path("comment/<str:listing_id>",views.comment,name="comment"),
    path("close/<str:listing_id>",views.close,name="close")
]
