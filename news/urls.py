from .views import newsView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('news/', newsView, name="news"),


]