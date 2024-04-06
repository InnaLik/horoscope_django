from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def leo(request):
    return HttpResponse('Лео')

def scorpio(request):
    return HttpResponse('Скорпион')