from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    url='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=743465dc458143aa816706415c58b57e'
    crypto_news = requests.get(url).json()

    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]


    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        
    my_list = zip(title, desc, img)

    context = {'my_list': my_list}

    return render(request, 'index.html', context)
@csrf_exempt
def search(request):
    url='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=743465dc458143aa816706415c58b57e'
    crypto_news = requests.get(url).json()

    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]


    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        my_list = zip(title, desc, img)
        if request.method=='POST':
            searching=request.POST['string']
            if searching in title:
                return render(request, 'search.html',{'my_list':my_list})
            else:
                return redirect('index')

    
        


