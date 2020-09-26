from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('title')
    serializer_class = OrderSerializer