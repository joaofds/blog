from django.shortcuts import render
from django.http import HttpResponse as Response

# Create your views here.
def index(request):
    return Response('Work fine')