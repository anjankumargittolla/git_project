from django.urls import path

from . import views

app_name = "app"


urlpatterns = [
    path("home/", views.home, name="home_page"),
    path("login/", views.token_login, name="login_page"),
    path("<name>/details/", views.rep_details, name="rep_details"),
]