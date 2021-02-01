from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# View
@login_required
def url_list(request):
    return render(
        request,
        'addresses/hello.html',
        {
            'message': "URL List",
        }
    )