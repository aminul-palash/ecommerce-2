from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
import accounts.urls
from .views import signup
from django.contrib.auth import views as auth_views



urlpatterns = [
   path('signup/', signup, name='signup'),
   path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]