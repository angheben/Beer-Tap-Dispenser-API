from django.urls import path, include
from .views import IndexBeer, CreateBeer, UpdateBeer, DeleteBeer, BeerAPIView

urlpatterns = [
    path("", IndexBeer.as_view(), name="index.html"),
    path("create_beer.html", CreateBeer.as_view(), name="create_beer"),
    path("update_beer.html", UpdateBeer.as_view(), name="update_beer"),
    path("delete_beer.html", DeleteBeer.as_view(), name="delete_beer"),

    path("beer_api.html", BeerAPIView.as_view(), name="beer_api"),
]