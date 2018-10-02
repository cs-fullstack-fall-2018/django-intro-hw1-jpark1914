from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def picker(request, color):
    if color == 'red':
        print('Fire'),
        return HttpResponse('Fire')
    elif color == 'blue':
        print('Sky'),
        return HttpResponse('Sky')
    else:
        print('Air'),
        return HttpResponse('Air')