# from django.shortcuts import render
# from django.views.generic import ListView
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# from .models import Item
# Create your views here.


class MenuListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
# class MenuList(ListView):
# model = Item
# template_name = 'item_list.html'
