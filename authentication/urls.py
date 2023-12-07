from django.contrib import admin
from django.urls import path, include
# from .views import home, login1, signup, signout, activate
from . import views

# urlpatterns = [
#     path('', home.as_view(), name='home'),
#     path('signup', signup.as_view(), name='signup'),
#     path('login1', login1.as_view(), name='login1'),
#     path('signout', signout.as_view(), name='signout'),   
#     path('activate/<str:uidb64>/<str:token>', activate.as_view(), name='activate'),
#     path('accounts/', include('allauth.urls'))
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login1', views.login1, name='login1'),
    path('signout', views.signout, name='signout'),   
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
    path('accounts/', include('allauth.urls'))
]
