from django.urls import path
from . import views

urlpatterns = [
    path('hello-medic', views.hello_medics, name='hello_medic'),
]