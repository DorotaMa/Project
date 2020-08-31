from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def medical(request):
    return render(request, 'medical/mainpage.html')