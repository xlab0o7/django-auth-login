from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from fooddiet import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str

from fooditems.models import Fooditems
from . tokens import generate_token

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
        myuser.is_active = False
        
        
        messages.success(request, 'Your Accounts has been created.')
        
        # For Email
        subject = 'Welcome to django project login system'
        message = f'Hey {myuser.first_name} !! \n Welcome to this django project login system. \n \n Thankyou for visiting our website.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(
            subject, 
            message, 
            from_email, 
            to_list
            )
        
        # For Email Verification
        
        current_site = get_current_site(request)
        email_sub = "Confirm your email @ login system at Django Project"
        msg = render_to_string('e-confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        
        email = EmailMessage(
            email_sub,
            msg,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.send()
        
        # myuser.save()
            
        return redirect('login1')
        
    return render(request, 'authentication/signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username-login')
        password = request.POST.get('pass-login')
    
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.get_username
            print(fname)
            return render(request, 'authentication/index.html', {'fname': fname})
            
        else:
            messages.error(request, 'Bad Credentials!')
            return redirect('home')
            
    return render(request, 'authentication/login.html')


def signout(request):
    logout(request)
    messages.success(request, "Successfully LOGGED OUT!!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')

    else:
        return render(request, 'activation_failed.html')