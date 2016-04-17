from django.shortcuts import render
from .serializers import *
from rest_framework import generics

# Create your views here.
class UserView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class TeamView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class KidView(generics.ListCreateAPIView):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer

class KidDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kid.objects.all()
    serializer_class = KidSerializer

class LeaderView(generics.ListCreateAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer

class LeaderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer

class BitacoraView(generics.ListCreateAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer

class BitacoraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer
