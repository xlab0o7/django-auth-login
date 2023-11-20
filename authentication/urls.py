from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login1', views.login1, name='login1'),
    path('signout', views.signout, name='signout'),
    path('accounts/', include('allauth.urls'))
]
