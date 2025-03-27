from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def hello_world(request):
    return JsonResponse({'message': 'hello world!'})

def test(tequest):
    return JsonResponse('This is test!')