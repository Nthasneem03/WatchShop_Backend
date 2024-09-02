from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import WatchSerializer  
from .models import Watch

# Create your views here.

def greet(request):  
    return HttpResponse("Hello, world!")


# To get a list of Watches
@api_view(['GET'])
def get_watch(request):  
    watches = Watch.objects.all()
    serializer = WatchSerializer(watches, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)


# To create a Watch
@api_view(['POST'])
def create_watch(request):  
    serializer = WatchSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
