from django.urls import path
from django.conf.urls import url


from . import views
from .views import pacjent_detail_view, update_personal_data

app_name = 'medical'

urlpatterns = [
    path('', views.medical, name="medical"),
    path('register', views.register, name="register"),
    path('mojedane',views.pacjent_detail_view, name="mojedane"),
    path('aktualizuj', views.update_personal_data, name="aktualizuj"),
    path('question', views.ask_question, name="question"),
    url(r'^calendar', views.CalendarView.as_view(), name='calendar'),
    path("update/<int:wizyta_id>", views.update, name="update"),
    path('', views.login_google, name='google_auth'),


]