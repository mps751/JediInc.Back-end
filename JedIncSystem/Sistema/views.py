from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rest_framework import generics
from .models import Projeto
from .serializers import ProjetoSerializer

class Projeto(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):

    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

