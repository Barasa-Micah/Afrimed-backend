from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def hello_medics(request):
    return Response({'message': 'Hello medic'})

@api_view(['GET'])
def view_users(request):
    return Response({'name': 'user'})

@api_view
def register_medic():
    pass
    #return Response({})