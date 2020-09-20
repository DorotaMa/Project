from django.urls import path
from django.conf.urls import url


from . import views

app_name = 'medical'

urlpatterns = [
    path('', views.medical, name="medical"),
    path('register', views.register, name="register"),
    path('userdetails', views.user_details, name="userdetails"),
    path('question', views.ask_question, name="question"),
    url(r'^calendar', views.CalendarView.as_view(), name='calendar'),
    path("update/<int:wizyta_id>", views.update, name="update"),

]