from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required()
def home(request):

    return render(request, 'monitoring/pages/home.html', context={
        "data": 85
    })


def detail(request):

    return 'AOLA'
    ...
