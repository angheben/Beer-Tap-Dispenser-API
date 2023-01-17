from django.shortcuts import render
from .models import Beer
from django.views.generic import ListView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BeerSerializer
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class IndexBeer(ListView):
    template_name = 'index.html'
    model = Beer
    queryset = Beer.objects.all()
    context_object_name = 'beers'


class BeerAPIView(APIView):
    """
    This class represent the API views of the beers
    """

    serializer_class = BeerSerializer

    def get(self, request, form=None):
        """
        This method serves to display the beers in the dispenser in the day
        """
        model = Beer
        beers = Beer.objects.all()
        times_used = Beer.objects.filter()
        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data)

    def put(self, request, pk, form=None):
        pass

    @action(detail=True ,methods=['post'])
    def post(self, request, pk, form=None):
        """
        This method serves to update the times_used variable when the dispenser be used, in other words, when the user
        click in the "Serve Beer" button, the times_used variable will be serialized and increase in one unit
        """
        beer = get_object_or_404(Beer, pk=pk)
        if request.method == 'POST':
            beer.total_cost = beer.cost_per_liter * beer.flow_volume
            beer.save()

        beer.times_used += int(request.data.get('times_used', 1))
        beer.save()
        serializer = BeerSerializer(beer)
        return Response(serializer.data)
