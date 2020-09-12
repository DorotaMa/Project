from django.urls import path


from . import views

urlpatterns = [
    path('', views.medical),
    path('register', views.register, name="register"),
    path('hello', views.hello, name="hello"),
    path('hello_login', views.hello_login, name='hello_login'),
]