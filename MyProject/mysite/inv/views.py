import requests
from requests.compat import quote_plus
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from . import models

BASE_CARIGSLIST_URL = 'https://singapore.craigslist.org/search/?query={}'

# Create your views here.
def home(request):
    return render(request,'base.html')

def search(request):
    srch = request.POST.get('txtsearch')
    models.Search.objects.create(search=srch)
    final_url = BASE_CARIGSLIST_URL.format(quote_plus(srch))
    response = requests.get(final_url)
    data = response.text
    #print (data)
    soupe = BeautifulSoup(data, features='html.parser')
    post_listings = soupe.find_all('li',{'class':'result-row'})

    final_postings = []
    for post in post_listings:

        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        final_postings.append((post_title,post_url,post_price))


    context_search = {
        'base_search':srch,
        'final_postings': final_postings,
    }
    return render(request, 'inv/search.html',context_search)