from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Check
from addresses.models import Address
from .forms import CheckForm

# View
@login_required
def check_list(request, url_id=None):

    # require an url
    if url_id == None:
        return HttpResponseRedirect(reverse("url:list"))

    checks = None
    checks = Check.objects.filter(
        url = url_id
    )

    return render(
        request,
        'check/list.html',
        {
            'checks': checks,
        }
    )

@login_required
def new_check(request, url_id=None):

    # request an url
    url = None
    try:
        url = Address.objects.get(
            Q(id = url_id),
            Q(owner = request.user)
        )
    except Check.DoesNotExist as e:
        return HttpResponseRedirect(reverse("url:list"))

    # require an url
    if url == None:
        return HttpResponseRedirect(reverse("url:list"))

    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            form.instance.url = url
            form.save()
            return HttpResponseRedirect(reverse("url:list"))

    form = CheckForm()
    return render(
        request,
        'utils/form.html',
        {
            'url_form': reverse("url:check:new", kwargs={'url_id':url_id}),
            'title': "New URL",
            'form':form,
        }
    )

@login_required
def edit_check(request, check_id=None):

    # require an id
    if check_id == None:
        return HttpResponseRedirect(reverse("url:list"))
    
    # get instance for that id
    current_instance = None
    try:
        current_instance = Check.objects.get(
            Q(id = check_id)
        )
    except Check.DoesNotExist as e:
        return HttpResponseRedirect(reverse("url:list"))
    
    # TODO : check if the user is the url owners

    # Handle Form response
    if request.method == 'POST':

        # TODO :  only the owner can edit

        # save in the database
        form = CheckForm(request.POST, instance=current_instance)
        if form.is_valid():
            form.save()
            # TODO redirect to the check list for that id 
            return HttpResponseRedirect(reverse("url:list"))


    form = CheckForm(instance=current_instance)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Edit Check",
            'form':form,
        }
    )