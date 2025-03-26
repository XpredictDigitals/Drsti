from django.http import JsonResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def add_controllers(request):
    if(request.method == 'GET'):
        return render(request,'add_controllers.html')
    else:
        return JsonResponse({'status':'error','message':'bad request'})