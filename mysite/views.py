from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("20231201073+陶颖")

def single_page(request):
    return render(request, 'page.html')