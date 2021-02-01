# coding: UTF-8
# Import du module views de l'application users
from addresses import views
from django.urls import path

app_name = 'addresses'
urlpatterns = [
    path('list/', views.url_list, name="list"),
]