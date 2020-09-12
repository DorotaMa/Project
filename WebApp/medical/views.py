from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def medical(request):
    return render(request, 'medical/mainpage.html')


def user_visits(request):
    return render(request, 'medical/user-visits.html')


def user_info(request):
    return render(request, 'medical/user-info.html')

