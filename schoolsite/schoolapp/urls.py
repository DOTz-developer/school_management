from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("login/",views.login_view,name = "login_view"),
    path("signup/",views.signup,name="signup"),
    path('logout/',views.logout,name = "logout"),
    path('preform/',views.pre_form,name = "pre_form"),
    path('preform/form',views.form,name = "form"),
    path('preform/logout',views.logout,name = "logout")



]
