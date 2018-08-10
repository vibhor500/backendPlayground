from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Text
from .serializers import TextSerializer
# Create your views here.

class TextView(APIView):
    def get(self,request):
        str = Text.hlloworld
        serializer = TextSerializer(many=False)
        return Response(serializer.data)
