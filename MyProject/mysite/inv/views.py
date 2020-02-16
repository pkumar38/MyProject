import requests

from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request,'base.html')

def search(request):
    srch = request.POST.get('txtsearch')
    context_search = {
        'base_search':srch,
    }
    return render(request, 'inv/search.html',context_search)