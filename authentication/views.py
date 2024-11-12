from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
# Create your views here.
class landView(View):
    def get(self, request):
        return render(request,'index.html')
    
class loginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
class signupView(View):
    def get(self, request):
        return render(request, 'authentication/signup.html')
    

# Username Field validation
class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should contain alphanumeric characters only'}, status=400)
        return JsonResponse({'username_valid':True})
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'sorry username already taken'}, status=409)
        return JsonResponse({'username_valid':True})
    

# Email Field validation
class EmailValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        email=data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'invalid email format'}, status=400)
        return JsonResponse({'email_valid':True})
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry the email has already been used'}, status=409)
        return JsonResponse({'email_valid':True})