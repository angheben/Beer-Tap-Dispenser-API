from django.urls import path, include
from .views import IndexBeer, BeerAPIView

urlpatterns = [
    path("", IndexBeer.as_view(), name="index.html"),
    path("beer_api.html", BeerAPIView.as_view(), name="beer_api"),
    path('api/beers/<int:pk>/', BeerAPIView.as_view(), name='beer_api')
]