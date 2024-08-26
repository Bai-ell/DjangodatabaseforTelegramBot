# institutions/views.py
from rest_framework import generics
from .models import Institution, Mta, ShortNamesMta
from .serializers import MtaSerializer, InstitutionSerializer, ShortNamesMtaSerializer

class InstitutionsListCreate(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    
class InstitutionsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class MTACreate(generics.ListCreateAPIView):
    queryset = Mta.objects.all()
    serializer_class = MtaSerializer

class MTARetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mta.objects.all()
    serializer_class = MtaSerializer

class ShortNamesMtaListCreate(generics.ListCreateAPIView):
    queryset = ShortNamesMta.objects.all()
    serializer_class = ShortNamesMtaSerializer

class ShortNamesMtaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShortNamesMta.objects.all()
    serializer_class = ShortNamesMtaSerializer