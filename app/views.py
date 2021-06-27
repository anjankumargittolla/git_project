"""This file is for declaring our business logic"""

from django.shortcuts import render

"""render is imported to use html """
from github import Github

"""To access the all the github methods"""
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
open_git = ""


def home(request):
    """This is for our home page"""
    return render(request, "app/home.html")


def details(request):
    """View for all required details """
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        global open_git
        open_git = Github(request.POST["token"])
        user_name = request.POST['username']
        user = open_git.get_user(user_name)
        print(user)
        request.session["username"] = user_name
        rep_list = user.get_repos()
        total = []
        for i in rep_list:
            total.append(i)
        return user_name, user, total


def token_login(request):
    """ View for login with personal token"""
    # import pdb
    # pdb.set_trace()
    username, user, total = details(request)
    print(username, user, total)
    return render(request, "app/repos.html", {"repos": total, "name": username})


def remove(request):
    """This is for logout function to clear the session"""
    request.session.delete()
    return HttpResponseRedirect("/app/home/")


def rep_details(request, name):
    """This is for repository contents"""
    username = open_git.get_user().login
    print(username)
    my_repo = open_git.get_repo("{}/{}".format(username, name))
    my_branches = list(my_repo.get_branches())
    print(request.POST)
    # import pdb
    # pdb.set_trace()
    if request.POST == "POST":
        contents = my_repo.get_contents("", ref=request.POST["source"])
        pulls = my_repo.get_pulls(state='open', sort='created', base=request.POST["source"])
    # elif len(request.POST) == 3:
    #     if request.method == "POST" and request.POST["delete"]:
    #         del_branch = request.POST["source"]
    #         ref = my_repo.get_git_ref("heads/{}".format(del_branch))
    #         ref.delete()
    #         contents = my_repo.get_contents("", ref="master")
    #         pulls = my_repo.get_pulls(state='open', sort='created', base="master")
    else:
        contents = my_repo.get_contents("", ref="master")
        pulls = my_repo.get_pulls(state='open', sort='created', base="master")
    files = []
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            files.extend(my_repo.get_contents(file_content.path))
        else:
            files.append(file_content)
    print(contents)
    return render(request, "app/repos_details.html",
                  {"branches": my_branches, "files": files, "repo": my_repo, "pulls": pulls})


def my_branch(request, name):
    username = open_git.get_user().login
    my_repo = open_git.get_repo("{}/{}".format(username, name))
    my_branches = list(my_repo.get_branches())
    return my_branches


def data(request, name):
    """View for give branch name and uploading a file """
    my_branches = my_branch(request, name)
    return render(request, "app/input.html", {"name": name, "branches": my_branches})


def branch(request, name):
    """For creating a new branch"""
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        repo_name = name
        source_branch = request.POST["source"]
        target_branch = request.POST["new_branch"]
        repo = open_git.get_user().get_repo(repo_name)
        new_commit = repo.get_branch(source_branch)
        repo.create_git_ref(ref='refs/heads/{}'.format(target_branch), sha=new_commit.commit.sha)
        return rep_details(request, name)
        # return render(request, "app/repos_details.html", {"name": name, "repo": repo, "branches": my_branches,
        #                                                   "files": files, "pulls": pulls})
    else:
        return render(request, "app/input.html", {"name": name})


def file_details(request, name):
    """Give file name from html"""
    repo_name = name
    my_branches = my_branch(request, name)
    repo = open_git.get_user().get_repo(repo_name)
    return render(request, "app/file.html", {"name": name, "branches": my_branches})


def file(request, name):
    """For creating a file in repository"""
    username = open_git.get_user().login
    my_repo = open_git.get_repo("{}/{}".format(username, name))
    my_branches = list(my_repo.get_branches())
    if request.method == "POST":
        repo = open_git.get_user().get_repo(name)
        file_name = request.FILES["file"]
        content = file_name.read()
        repo.create_file(file_name.name, request.POST["msg"], content, branch=request.POST["source"])
        # return HttpResponseRedirect("/app/name/details/")
        return rep_details(request, name)
    else:
        return render(request, "app/file.html", {"name": name, "branches": my_branches})


def pull(request, name):
    """View for giving inputs to create a pull request"""
    username = open_git.get_user().login
    my_branches = my_branch(request, name)
    return render(request, "app/pull.html", {"name": name, "branches": my_branches})


def pull_request(request, name):
    repo = open_git.get_user().get_repo(name)
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        head = request.POST["head"]
        base = request.POST["source"]
        new_pr = repo.create_pull(title=title, body=body, head=head, base=base)
        print(new_pr)
        return rep_details(request, name)
    else:
        return pull(request, name)


def merge_input(request, name):
    """To give the those two branches which has to be merged"""
    my_branches = my_branch(request, name)
    return render(request, "app/merge.html", {"branches": my_branches, "name": name})


def merge(request, name):
    """To merge the branches"""
    username = open_git.get_user().login
    my_repo = open_git.get_repo("{}/{}".format(username, name))
    if request.method == "POST":
        try:
            target_branch = my_repo.get_branch(request.POST["target"])
            source_branch = my_repo.get_branch(request.POST["source"])
            # import pdb
            # pdb.set_trace()
            merge_to_master = my_repo.merge(source_branch, target_branch, "merge to {}".format(target_branch))
        except Exception as ex:
            print(ex)
        return rep_details(request, name)
    else:
        return merge_input(request, name)


def delete_branch(request, name):
    """View for delete perticular branch"""
    my_branches = my_branch(request, name)
    return render(request, "app/delete_branch.html", {"branches": my_branches, "name": name})


def delete(request, name):
    repo = open_git.get_user().get_repo(name)
    if request.method == "POST":
        del_branch = request.POST["source"]
        ref = repo.get_git_ref("heads/{}".format(del_branch))
        ref.delete()
        return rep_details(request, name)
    else:
        return delete_branch(request, name)