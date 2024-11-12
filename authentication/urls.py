from .views import loginView,signupView,EmailValidationView,UsernameValidationView,landView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    
    path('login',loginView.as_view(), name="login" ),
    path('signup', signupView.as_view(), name="signup"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
]
