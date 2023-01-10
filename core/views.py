from django.shortcuts import render
from .models import Beer
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from .serializer import BeerSerializer
from rest_framework import status


class IndexBeer(ListView):
    template_name = 'index.html'
    model = Beer
    queryset = Beer.objects.all()
    context_object_name = 'beer'


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

    def get_stock_beer(self, request, form=None):
        """
        This method serves to display the beers in the dispenser in the day
        :param request: API
        :return: The beers in stock
        """

