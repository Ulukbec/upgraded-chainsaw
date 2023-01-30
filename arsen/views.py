from django.shortcuts import render, HttpResponse


# Create your views here.

def product_view(request):
    return HttpResponse(request, "Hello world !!")




def products(request):
    return HttpResponse(request, "huuui")
