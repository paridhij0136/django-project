from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
 path("", views.index, name='index'),
    path("furm.html/", views.register, name='register'),
    path("login.html/", views.login_page, name='login'),
    path("signup.html/", views.signup_page, name='signup_page'),
    path("login/", views.login_user, name="login"),
    path("signup/", views.signup_view, name="signup"),   
]
