from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from drfapp.api import views
from drfapp.models import Account, Cinema
from drfapp.api.serializers import AccountSerializer, CinemaSerializer

class AccountList(APIView):
       
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class AccountDetails(APIView):
      
    def get(self, request, pk):
        lord = Account.objects.get(pk=pk)
        serializer_class = AccountSerializer(lord)
        return Response(serializer_class.data)

    def put(self, request, pk):
        lords = Account.objects.get(pk=pk)
        serializer = AccountSerializer(lords, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        

    def delete(self, request, pk, format=None):
        good = Account.objects.get(pk=pk)
        good.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CinemaList(APIView):
    
    
    def get(self, request):
        accounts = Cinema.objects.all()
        serializer = CinemaSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           