from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .serializers import stockserializer
# Create your views here.

class stocklist(APIView):

    def get(self,request):
        stocks= stock.objects.all()
        serializer = stockserializer(stocks,many=True)
        return Response(serializer.data)


    
