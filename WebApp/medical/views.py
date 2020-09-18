from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from . import forms
from django.shortcuts import redirect
# Create your views here.
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

from .forms import AskingQuestion
from django.core.mail import send_mail


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


class CalendarView(generic.ListView):
    model = Wizyta
    template_name = 'medical/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and month
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


# Formularz kontaktowy do lekarza


def ask_question(request):
    sent = False
    if request.method == 'POST':
        form = AskingQuestion(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Pacjent {cd['name']} {cd['surname']} pragnie zadać pytanie"
            message = f"Dane pacjenta:\nImię: {cd['name']} Nazwisko: {cd['surname']}\nAdres e-mail: {cd['email']}\n\n" \
                      f"Pytanie:\n{cd['message']}"
            send_mail(subject, message, cd['email'], 'admin_lekarz@strona.pl')

            # dodać poprawny ades e-mail

            sent = True

    else:
        form = AskingQuestion()

    return render(request, 'medical/question.html', {'form': form, 'sent': sent})



# @require_http_methods(["GET", "POST"])
def update(request, wizyta_id):

    w = Wizyta.objects.get(pk=wizyta_id)

    if request.method == "GET":
        return render(request, 'medical/update.html', {
            "wizyta": w,
        })

    else:
        # U (Update) z CRUD
        w.text = request.POST.get("wizyta")
        w.save()

        return redirect("medical:calendar")