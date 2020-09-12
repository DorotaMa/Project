from django.urls import path

from . import views

urlpatterns = [
    path('', views.medical),
    path('user-info', views.user_info),
    path('user-visits', views.user_visits),
]
