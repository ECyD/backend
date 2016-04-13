from django.shortcuts import render
from .serializers import *
from rest_framework import generics

# Create your views here.
class UserView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = DefaultMyUserSerializer
