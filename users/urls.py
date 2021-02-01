# coding: UTF-8
# Import du module views de l'application users
from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
]