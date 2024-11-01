from django.urls import path
from authorsapp import views

app_name = 'authorsapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add-author/', views.addAuthor, name='add-author'),
    path('<str:author_id>', views.getAuthor, name='get-author'),

]
