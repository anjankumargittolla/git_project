"""This file is for declaring our business logic"""

from django.shortcuts import render

"""render is imported to use html """
from github import Github

"""To access the all the github methods"""
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import json


# Create your views here.


def home(request):
    """This is for our home page"""
    return render(request, "app/home.html")


open_git = ""
username = ""


def token_login(request):
    """ View for login with personal token"""
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        global open_git
        open_git = Github(request.POST["token"])
        global username
        username = request.POST['username']
        user = open_git.get_user(username)
        request.session["username"] = username
        # users = user.login
        rep_list = user.get_repos()
        total = []
        for i in rep_list:
            total.append(i)
        return render(request, "app/repos.html", {"repos": total, "name": username})


def remove(request):
    """This is for logout function to clear the session"""
    request.session.delete()
    return HttpResponseRedirect("/app/home/")


def rep_details(request, name):
    """This is for repository contents"""
    import pdb
    pdb.set_trace()
    print(username, "=========\n", name)
    print(type(open_git))
    my_repo = open_git.get_repo("{}/{}".format(username, name))
    my_branches = list(my_repo.get_branches())
    print(my_branches)
    contents = my_repo.get_contents("")
    files = []
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(my_repo.get_contents(file_content.path))
        else:
            files.append(file_content)
    # print(contents)
    return render(request, "app/repos_details.html", {"branches": my_branches, "files": files, "repo": my_repo})


def branch(request, name):
    """For creating a new branch"""
    pass
