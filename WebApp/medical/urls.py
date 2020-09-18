from django.urls import path
from django.conf.urls import url


from . import views

app_name = 'medical'

urlpatterns = [
    path('', views.medical),
    path('register', views.register, name="register"),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar')
]