from django.shortcuts import render
from django.shortcuts import reverse
from . import forms
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


def medical(request):
    return render(request, 'medical/mainpage.html')


def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse("hello"))
    else:
        form = forms.RegisterForm()
    return render(request, 'medical/register.html', {"form": form})


def hello(request):
    return render(request, "medical/mainpage.html")


def hello_login(request):
    return render(request, "medical/mainpage.html")