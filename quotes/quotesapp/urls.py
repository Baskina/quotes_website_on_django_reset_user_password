from django.urls import path
from quotesapp import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('page/<int:page>', views.main, name='main_paginate'),
    path('add-quote/', views.addQuote, name='add-quote'),
]
