from datetime import datetime
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

from django.core.mail import send_mail

from .forms import AskingQuestion
from .models import *
from .utils import Calendar
from . import forms
import datetime
from .forms import UserDetails


# Create your views here.


def medical(request):
    return render(request, 'medical/mainpage.html')


def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            created_user = User.objects.get(id=user.id)
            id_user=created_user.id
            return redirect('medical:aktualizuj', id_user)
    else:
        form = forms.RegisterForm()
    return render(request, 'medical/register.html', {"form": form})


def pacjent_detail_view(request):
    obj = Pacjent.objects.get(user=request.user)
    wizyty = Wizyta.objects.filter(pacjent_id=obj.id)
    # dzisiaj = datetime.datetime.now()
    context = {
        'object': obj,
        'wizyty': wizyty,
        # 'dzisiaj': dzisiaj,
    }
    return render(request, "medical/mojedane.html", context)


def update_pacient_data(request, id_user):
    user = User.objects.get(id=id_user)
    print(user)
    form = UserDetails(request.POST or None)
    if form.is_valid():
        newuser = form.save(commit=False)
        newuser.user = user
        newuser.save()
        return redirect('medical:medical')
    return render(request, "medical/aktualizuj.html", {'form': form})


def change_patient_data(request):
    form = forms.UserDetails(request.POST)
    if form.is_valid():
        user = Pacjent.objects.get(user=request.user)
        user.imie = request.POST.get("imie")
        user.nazwisko = request.POST.get("nazwisko")
        user.numer_telefonu = request.POST.get("numer_telefonu")
        user.rok_urodzenia = request.POST.get("rok_urodzenia")
        user.plec = request.POST.get("plec")

        user.save()
        return redirect(reverse('medical:medical'))

    return render(request, "medical/zmiendane.html", {'form': form})


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()


# @require_http_methods(["GET", "POST"])
def booking_appointment(request, wizyta_id):
    w = Wizyta.objects.get(pk=wizyta_id)

    if request.method == "GET":
        return render(request, 'medical/update.html', {
            "wizyta": w,
        })

    else:
        # U (Update) z CRUD
        w.pacjent = Pacjent.objects.get(user=request.user)
        w.notes = request.POST.get("notes")
        w.save()

        return redirect("medical:calendar")


@require_http_methods(["POST"])
def cancel_appointment(request, wizyta_id):
    wizyta = Wizyta.objects.get(pk=wizyta_id)
    wizyta.pacjent = None
    wizyta.save()
    return redirect("medical:mojedane")


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
            send_mail(subject, message, cd['email'], ['admin_lekarz@strona.pl'])

            sent = True
            return redirect('./')
    else:
        form = AskingQuestion()
    return render(request, 'medical/question.html', {'form': form, 'sent': sent})


# logowanie google

def login_google(request):
    return render(
        request,
        'google_auth/login.html',
    )


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
