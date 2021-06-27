"""All urls are mentioned here or every function"""
from django.urls import path

"""To give the path for every functionality"""
from . import views

"""Views are imported from app or mapping with urls"""

app_name = "app"

urlpatterns = [
    path("home/", views.home, name="home_page"),
    path("login/", views.token_login, name="login_page"),
    path("<name>/details/", views.rep_details, name="rep_details"),
    path("<name>/data/", views.data, name="data"),
    path("<name>/create_branch/", views.branch, name="branch"),
    path("<name>/file/", views.file, name="file"),
    path("<name>/upload/", views.file_details, name="file_details"),
    path("<name>/create_pr/", views.pull, name="pull"),
    path("<name>/submit_pr/", views.pull_request, name="pull_request"),
    path("logout/", views.remove, name="logout"),
    path("<name>/merge_inputs/", views.merge_input, name="merge_input"),
    path("<name>/merge/", views.merge, name="merge"),
    path("<name>/delete_branch/", views.delete_branch, name="delete_branch"),
    path("<name>/delete/", views.delete, name="delete"),
]
