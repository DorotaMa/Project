from django.urls import path
from django.conf.urls import url


from . import views
from django.urls import include
app_name = 'medical'

urlpatterns = [
    path('', views.medical),
    path('register', views.register, name="register"),
    path('question', views.ask_question, name="question"),
    url(r'^calendar', views.CalendarView.as_view(), name='calendar'),
    path("update/<int:wizyta_id>", views.update, name="update"),
    path('', views.login_google, name='google_auth')
]