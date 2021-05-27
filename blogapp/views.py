from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.forms import UserCreationForm

from .forms import signup, loginforms, Postform
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.

from .models import Post

from django.contrib.auth.models import Group

def home(request):
    return render(request, 'html/home.html', {'owner': 'Made by Sonu Sharma'})

def about(request):
    return render(request, 'html/about.html')

def contact(request):
    if request.method == "POST":
        contactus = contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        summary=request.POST.get('summary')
        contactus.name = name
        contactus.email = email
        contactus.summary = summary
        contactus.save()
        return HttpResponse("<h1>We get back to you Soon!<h1>")
    return render(request, 'html/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'html/dashboard.html', {'post': post, 'name': full_name, 'groups': gps})
    else:
        return HttpResponseRedirect('/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == "POST":
        form = signup(request.POST)
        if form.is_valid():
            # messages.success(request, 'Thanks for Register')
            user =  form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/login')
    else:
        form = signup()
    return render(request, 'html/signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginforms(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Succefully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = loginforms()
        return render(request, 'html/login.html', {'login': form})
    else:
        return HttpResponseRedirect('/dashboard/')

def add_blog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Postform(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                postsave = Post(title=title, desc=desc)
                postsave.save()
                form = Postform()
        else:
            form = Postform()
        return render(request, 'html/newblog.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

def update_blog(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            postid = Post.objects.get(pk=id)
            form = Postform(request.POST, instance=postid)
            if form.is_valid():
                form.save()
        else:
            postid = Post.objects.get(pk=id)
            form = Postform(instance=postid)
        return render(request, 'html/updateblog.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')
    
def delete_blog(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            postid = Post.objects.get(pk=id)
            postid.delete()
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')