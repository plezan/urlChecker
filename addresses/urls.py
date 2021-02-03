# coding: UTF-8
# Import du module views de l'application users
from addresses import views
from django.urls import path, include

import check

app_name = 'addresses'
urlpatterns = [
    path('list/', views.url_list, name="list"),
    path('new/', views.new_url, name="new"),
    path('edit/<int:url_id>', views.edit_url, name="edit"),
    path(r'check/', include('check.urls', namespace='check')),
]

