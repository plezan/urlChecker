# coding: UTF-8
# Import du module views de l'application users
from check import views
from django.urls import path

app_name = 'check'
urlpatterns = [
    path('<int:url_id>/list/', views.check_list, name="list"),
    path('<int:url_id>/new/', views.new_check, name="new"),
    path('edit/<int:check_id>', views.edit_check, name="edit"),
]