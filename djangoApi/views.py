from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
def hello_world(request):
    return JsonResponse({'message': 'hello world!'})

def test(request):
    return HttpResponse("This is a test!")