# Import
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import UserProfile

DEFAULT_PAGE_AFTER_LOGIN = "url:list"
DEFAULT_PAGE_AFTER_LOGOUT = "users:login"

# View
def hello(request):
    return render(
        request,
        'users/hello.html',
        {
            'message': "Welcome to URL Checker",
        }
    )

def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse(DEFAULT_PAGE_AFTER_LOGIN))
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['raw_password']
        
            user = UserProfile.objects.create_user(
                username=username,
                email=email,
                password=raw_password,
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse(DEFAULT_PAGE_AFTER_LOGIN))
    
    else:
        form = RegisterForm()
    
    return render(
        request,
        'utils/form.html',
        {
            'url_form': reverse("users:register"),
            'title': "Sign up",
            'form':form,
        })


def login_view(request):

    # ignore if authentificated
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse(DEFAULT_PAGE_AFTER_LOGIN))

    # Handle login requests
    if 'username' in request.POST and 'password' in request.POST:
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )
        
        # Handle authentification failure
        if user is None:
            return render(
                request,
                'users/login.html',
                {
                    "auth_error": True,
                }
            )

        # Succesfull authentification
        login(request, user)
    
        if request.GET.get('next') is not None:
            return redirect(request.GET['next'])
        else:
            return HttpResponseRedirect(reverse(DEFAULT_PAGE_AFTER_LOGIN))
        
            
    # default login renderrer
    return render(
        request,
        'users/login.html',
        {}
    )


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(DEFAULT_PAGE_AFTER_LOGOUT))