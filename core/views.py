from django.shortcuts import render
from .models import Beer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BeerSerializer
from rest_framework import status


class IndexBeer(ListView):
    template_name = 'index.html'
    model = Beer
    queryset = Beer.objects.all()
    context_object_name = 'beers'


class CreateBeer(CreateView):
    template_name = 'create_beer'
    model = Beer
    reverse_lazy = 'index'


class UpdateBeer(UpdateView):
    template_name = 'update_beer'
    model = Beer
    reverse_lazy = 'index'


class DeleteBeer(DeleteView):
    template_name = 'delete_beer'
    model = Beer
    success_url = 'index'


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

    def put(self, request, form=None):
        """
        This method serves to update the times_used variable when the dispenser be used
        """
        model = Beer
        times_used = Beer.objects.update_or_create(times_used=times_used + 1)
        serializer = BeerSerializer(times_used, many=True)
        return Response(serializer.data)
