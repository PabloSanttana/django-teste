from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, 'monitoring/pages/home.html', context={
        "data": 85
    })


def detail(request):

    return 'AOLA'
    ...
