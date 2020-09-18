from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponse
from . import forms
from django.shortcuts import redirect
# Create your views here.


def medical(request):
    return render(request, 'medical/mainpage.html')


def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('medical'))
    else:
        form = forms.RegisterForm()
    return render(request, 'medical/register.html', {"form": form})



from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Wizyta
    template_name = 'medical/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()

