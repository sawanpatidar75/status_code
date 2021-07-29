from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('search-url',views.Search_Url,name='search-url'),
    path('search-graph',views.Search_graph,name='search-graph'),
    
]