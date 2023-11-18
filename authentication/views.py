from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
        
        print(username, email, password)
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, 'Your Accounts has been created.')
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
            return redirect('signup')
            
    return render(request, 'authentication/login.html')


def signout(request):
    logout(request)
    return redirect('login1')
