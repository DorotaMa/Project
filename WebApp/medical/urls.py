from django.urls import path
from django.conf.urls import url


from . import views
from .views import pacjent_detail_view, update_pacient_data, booking_appointment, cancel_appointment, change_patient_data

app_name = 'medical'

urlpatterns = [
    path('', views.medical, name="medical"),
    path('register', views.register, name="register"),
    path('mojedane',views.pacjent_detail_view, name="mojedane"),
    path('aktualizuj/<int:id_user>', views.update_pacient_data, name="aktualizuj"),
    path('zmiendane', views.change_patient_data, name="zmiendane"),
    path('question', views.ask_question, name="question"),
    url(r'^calendar', views.CalendarView.as_view(), name='calendar'),
    path("update/<int:wizyta_id>", views.booking_appointment, name="update"),
    path("delete/<int:wizyta_id>", views.cancel_appointment, name="delete"),
    path('', views.login_google, name='google_auth'),


]