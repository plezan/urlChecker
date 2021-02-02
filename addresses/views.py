from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Address
from .forms import UrlForm

# View
@login_required
def url_list(request):
    urls = None
    urls = Address.objects.filter(
        owner = request.user
    )

    return render(
        request,
        'addresses/list.html',
        {
            'urls': urls,
        }
    )

@login_required
def new_url(request):
    
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse("url:list"))

    form = UrlForm()
    return render(
        request,
        'utils/form.html',
        {
            'url_form': reverse("url:new"),
            'title': "New URL",
            'form':form,
        }
    )

@login_required
def edit_url(request, url_id=None):

    # require an id
    if not url_id:
        return HttpResponseRedirect(reverse("url:list"))
    
    # get instance for that id
    current_instance = None
    try:
        current_instance = Address.objects.get(
            Q(id = url_id),
            Q(owner = request.user),
        )
    except Address.DoesNotExist as e:
        return HttpResponseRedirect(reverse("url:list"))

    # Handle Post
    if request.method == 'POST':

        # only the user can edit
        if(current_instance.owner != request.user):
            return HttpResponseRedirect(reverse("url:list"))

        # save in the database
        form = UrlForm(request.POST, instance=current_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("url:list"))


    form = UrlForm(instance=current_instance)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Edit URL",
            'form':form,
        }
    )