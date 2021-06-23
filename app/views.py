"""This file is for declaring our business logic"""

from django.shortcuts import render

"""render is imported to use html """
from github import Github

"""To access the all the github methods"""
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def home(request):
    """This is for our home page"""
    return render(request, "app/home.html")


open_git = ""
username = ""
files = ""
my_branches = ""


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
    print(username, "=========\n", name)
    print(type(open_git))
    my_repo = open_git.get_repo("{}/{}".format(username, name))
    global my_branches
    my_branches = list(my_repo.get_branches())
    print(my_branches)
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        contents = my_repo.get_contents("", ref=request.POST["branch"])
    else:
        contents = my_repo.get_contents("", ref="master")
    global files
    files = []
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            files.extend(my_repo.get_contents(file_content.path))
        else:
            files.append(file_content)
    print(contents)
    return render(request, "app/repos_details.html", {"branches": my_branches, "files": files, "repo": my_repo})


def data(request, name):
    """View for give branch name and uploading a file """
    # my_repo = open_git.get_repo("{}/{}".format(username, name))
    return render(request, "app/input.html", {"name": name, "branches": my_branches})


def branch(request, name):
    """For creating a new branch"""
    if request.method == "POST":
        import pdb
        pdb.set_trace()
        repo_name = name
        source_branch = request.POST["branch"]
        target_branch = request.POST["new_branch"]
        repo = open_git.get_user().get_repo(repo_name)
        new_commit = repo.get_branch(source_branch)
        repo.create_git_ref(ref='refs/heads/{}'.format(target_branch), sha=new_commit.commit.sha)
        return render(request, "app/repos_details.html", {"name": name, "repo": repo, "branches":my_branches,
                                                          "files": files})
    else:
        return render(request, "app/input.html", {"name": name})


def file_details(request, name):
    """Give file name from html"""
    return render(request, "app/file.html", {"name": name, "branches":my_branches})


def file(request, name):
    """For creating a file in repository"""
    import pdb
    pdb.set_trace()
    if request.method == "POST":
        repo = open_git.get_user().get_repo(name)
        repo.create_file(request.FILES["file"], request.POST["msg"], request.POST["commit"],
                         branch=request.POST["branch"])
        return HttpResponse("file uploaded successfully")
    else:
        return render(request, "app/file.html", {"name": name, "branches": my_branches})


def pull(request, name):
    """View for giving inputs to create a pull request"""
    return render(request, "app/pull.html", {"name": name, "branches": my_branches})


def pull_request(request, name):
    repo = open_git.get_user().get_repo(name)
    if request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        head = request.POST["head"]
        base = request.POST["base"]
        new_pr = repo.create_pull(title=title, body=body, head=head, base=base)
        print(new_pr)
        return HttpResponse("success")
    else:
        return render(request, "app/pull.html", {"name": name, "branches": my_branches})