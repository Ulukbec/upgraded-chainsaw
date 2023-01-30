from django.shortcuts import render, HttpResponse


# Create your views here.

def product_view(request):
    return HttpResponse(request, "Hello world !!")




def prodsucats(request):
    return HttpResponse(request, "huuui")
