from django.urls import path
from . import views

urlpatterns=[
    path("/signup/",views.initial,name="initial"),
    path("/sign/",views.sign_up,name="sign_up"),
    path("/homepage/",views.home,name="home"),
    path("/login/",views.log,name="log"),
    path("/logged_in/",views.log_in,name="log_in"),
]
