from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/list_detail.html')

def bea_table(request):
    return render(request, 'blog/table.html')