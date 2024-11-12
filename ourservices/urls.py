from .views import servicesView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('services/', servicesView, name="services"),


]