from django.urls import include, path

from . import views

urlpatterns = [
    # path('patient/', include('patient.urls'))
    path("", views.index, name="index"),
]
