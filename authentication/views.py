from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from fooddiet import settings
from django.shortcuts import resolve_url
from allauth.account.views import confirm_email

def confirm_email(request, **kwargs):
    response = confirm_email(request, **kwargs)
    if response.status_code == 302:
        success_url = resolve_url('account_email_confirmation_success')
        response['Location'] = success_url

    return response
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')


def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username-signup')
        email = request.POST.get('email-signup')
        fname = request.POST.get('fname-signup')
        lname = request.POST.get('lname-signup')
        password = request.POST.get('pass-signup')
        
        # print(username, email, password)
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('home')
            
        if User.objects.filter(email=email):
            messages.error(request, "Email already taken by user!")
            return redirect('home')
        if len(username) > 15:
            messages.error(request, "Username must be under 15 characters.")
        
        if not username.isalnum():
            messages.error(request, "Username must be aplhanumberic")
            
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, 'Your Accounts has been created.')
        
        # For Email
        subject = 'Welcome to django project login system'
        message = f'Hey,{myuser.first_name} !! \n Welcome to this django project login system. \n \n Thankyou for visiting our website.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list)
        
        # , fail_silently = True
        
        return redirect('login1')
        
    return render(request, 'authentication/signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username-login')
        password = request.POST.get('pass-login')
    
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})
            
        else:
            messages.error(request, 'Bad Credentials!')
            return redirect('home')
            
    return render(request, 'authentication/login.html')


def signout(request):
    logout(request)
    messages.success(request, "Successfully LOGGED OUT!!")
    return redirect('home')
