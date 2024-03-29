from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medicapi.views import MedicViewSet

router = DefaultRouter()
router.register(r"medics", MedicViewSet)

urlpatterns = [
    #path("patient/", include('patient.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

