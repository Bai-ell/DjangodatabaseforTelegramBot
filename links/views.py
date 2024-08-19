from rest_framework import generics
from .models import Links, Contats
from .serializers import LinksSerializer, ContatsSerializer

class LinksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class LinksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class ContatsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contats.objects.all()
    serializer_class = ContatsSerializer

class ContatsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contats.objects.all()
    serializer_class = ContatsSerializer
