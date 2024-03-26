from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path("patient/", include('patient.urls')),
    path('admin/', admin.site.urls),
    path('medicapi/', include('medicapi.urls'))
]

