"""This file is for declaring our business logic"""

from django.shortcuts import render
"""render is imported to use html """
from github import Github
"""To access the all the github methods"""
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    """This is for our home page"""
    return render(request, "app/home.html")


open_git = ""


def token_login(request):
    """ View for login with personal token"""
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        global open_git
        open_git = Github(request.POST["token"])
        username = request.POST['username']
        user = open_git.get_user(username)
        # request.session["open_git"] = open_git
        # request.session["username"] = username
        rep_list = user.get_repos()
        total = []
        for i in rep_list:
            total.append(i)
        return render(request, "app/repos.html", {"repos": total, "name": username})


def rep_details(request, name):
    """This is for repository contents"""
    # import pdb
    # pdb.set_trace()
    # another_git = request.session["open_git"]
    # name = request.session["username"]
    # open_git, username = git_hub(request)
    # repo = open_git.get_repo("{}/{}".format(username, name))
    # a = list(repo.get_branches())
    # return HttpResponse("anjan,{}".format(name), a)
    # print(another_git, name)
    print(open_git,"----------------------")
    return HttpResponse("success")