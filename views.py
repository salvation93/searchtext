from django.shortcuts import render

import requests

from bs4 import BeautifulSoup as bs


# Create your views here.

def home(request):

    return render(request, 'index.html')

 

def search(request):

    if request.method == "POST":

        search = request.POST['search']

        url = 'https://www.ask.com/web?q='+search # using web scraping from here below to get the result

        res = requests.get(url)

        soup = bs(res.text, 'lxml')

        result_list = soup.find_all('div', {'class':'PartialSearchResults-item'})

        final_result = []

        for result in result_list:

            result_title = result.find(class_='PartialSearchResults-item-title').text

            result_url = result.find('a').get('href')

            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((result_title, result_url, result_desc))
            print(result_title)

        context = {

            'final_result':final_result

        }

        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html')