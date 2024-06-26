from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Medics
from .serializers import MedicSerializer
# Create your views here.
@api_view(['GET'])
def hello_medics(request):
    return Response({'message': 'Hello medic'})

class MedicViewSet(viewsets.ModelViewSet):
    queryset = Medics.objects.all()
    serializer_class = MedicSerializer

@api_view
def register_medic():
    pass
    #return Response({})