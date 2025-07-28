from django.shortcuts import render
from rest_framework import viewsets

from shop.models import Shop


# Create your views here.
# class ShopViewSet(viewsets.ModelViewSet):
#     """ view to create update and return a shop. """
#     queryset = Shop.objects.all()
#     serializer_class =