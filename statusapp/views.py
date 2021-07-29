from django.core.checks import messages
from django.shortcuts import render, redirect
from matplotlib import pyplot as plt
from requests.api import request
import requests
from requests.exceptions import HTTPError
from django.contrib import messages
from . models import *
import requests,random
from datetime import datetime
from time import time,sleep
from .utils import get_plot
from itertools import count

# Create your views here.

def Index(request):
    return render(request, 'html/index.html')

x = []
y = []
index = count()
def Search_Url(request):    
    print(x)
    print(y)

    if request.method=="POST":
        while True:
                try:
                    url = request.POST['url-search']
                    global copyurl
                    copyurl = url
                    if 'http' in url :
                      
                        stts = requests.head(url)
                        if stts.status_code == 200:
                            x.append(200)
                            y.append(next(index))
                        elif stts.status_code == 500:
                            x.append(500)
                            y.append(next(index))
                        else:
                            x.append(0)
                            y.append(next(index))

                        time = datetime.now()
                        print(stts)
                        context = {'url':url,'stts':stts,'time':time}
                        return render(request,'html/base.html',context)
                        
                    elif url:
                        url = ('https://www.{}.com'.format(url))
                        stts = requests.head(url)
                        if stts.status_code == 200:
                            x.append(200)
                            y.append(next(index))
                        elif stts.status_code == 500:
                            x.append(500)
                            y.append(next(index))
                        else:
                            x.append(0)
                            y.append(next(index))

                        time = datetime.now()
                        context = {'url':url,'stts':stts,'time':time}
                        return render(request,'html/base.html',context)
                    else:
                        return redirect('search-url')
                except HTTPError:
                    x.append(0)
                    y.append(next(index))
                    messages.info(request, 'Please Enter Valid Url.')
                    return redirect('index')

                except Exception:
                    x.append(0)
                    y.append(next(index))
                    messages.info(request, 'Please Enter Valid Url.')
                    return redirect('index')
    print(x)
    print(y)
    return render(request,'html/base.html')


def Search_graph(request):
    chart = get_plot(y,x)
   
    urls = copyurl
    
    while True:
        
        try:
            # copy_url = request.POST['url-search']
            if 'http' in urls :
               
                stts = requests.head(urls)
                if stts.status_code == 200:
                    x.append(200)
                    y.append(next(index))
                elif stts.status_code == 500:
                    x.append(500)
                    y.append(next(index))
                else:
                    x.append(0)
                    y.append(next(index))
                time = datetime.now()
                print(stts)
                context = {'url':urls,'stts':stts,'time':time,'chart':chart}
                return render(request,'html/base.html',context)
                
            elif urls:
                
                copy_url = ('https://www.{}.com'.format(urls))
                stts = requests.head(copy_url)
                if stts.status_code == 200:
                    x.append(200)
                    y.append(next(index))
                elif stts.status_code == 500:
                    x.append(500)
                    y.append(next(index))
                else:
                    x.append(0)
                    y.append(next(index))
                time = datetime.now()
                context = {'url':copy_url,'stts':stts,'time':time,'chart':chart}
                return render(request,'html/base.html',context)
            else:
                return redirect('search-url')
        except HTTPError:
            x.append(0)
            y.append(next(index))
            messages.info(request, 'Please Enter Valid Url.')
            return redirect('index')

        except Exception:
            x.append(0)
            y.append(next(index))
            messages.info(request, 'Please Enter Valid Url.')
            return redirect('index')



   

    
