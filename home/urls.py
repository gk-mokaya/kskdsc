from .views import homeView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
   path('', homeView, name="home"), 
]

