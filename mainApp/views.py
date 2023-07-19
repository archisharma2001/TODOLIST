from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import *
from mainApp.forms import TODOForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    return render(request,"index.html") 


@login_required(login_url="/login/") #user can't create todo without login 
def addnewPage(request):
    if request.user.is_authenticated: 
        user= request.user
        form= TODOForm()
        todos= TODO.objects.filter(user= user).order_by('priority')
        return render(request,"addnew.html", context={'form': form, 'todos': todos})

#to add new todo items 
def add_todo(request):
    if request.user.is_authenticated: 
        user= request.user
        form = TODOForm(request.POST)
        print(user)
        if form.is_valid():
            print(form.cleaned_data)
            todo= form.save(commit=False)
            todo.user= user
            todo.save()
            return HttpResponseRedirect('/addnew/')
        else:
            return render(request, 'addnew.html', context={'form': form})
 # delete existing dod
def delete_todo(request,id):
    TODO.objects.get(pk= id).delete()
    return redirect('/addnew/')


#register to access
def registerPage(Request):

    if Request.method == "POST":
        first_name= Request.POST.get('first_name')
        last_name= Request.POST.get('last_name')
        username= Request.POST.get('username')
        password= Request.POST.get('password')

        user= User.objects.filter(username = username)

        if user.exists():
            messages.info(Request, "User name already taken try some other name")
            return HttpResponseRedirect('/register/')

        user= User.objects.create(
            first_name= first_name,
            last_name= last_name,
            username= username,
        )
        user.set_password(password)
        user.save()
        messages.info(Request, "User created Successfully")

        return HttpResponseRedirect('/login/')

    return render(Request,"register.html")

#login befor add todo 
def loginPage(Request):
          
    if Request.method == 'POST':
        username= Request.POST.get('username')
        password= Request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            
            messages.error(Request,"Invalid User Name ")
            return HttpResponseRedirect('/login/')
    
        user = authenticate(username = username , password = password )

        if user is None:
            messages.error(Request,"Invalid Password")
            return HttpResponseRedirect('/login/')
        
        else:
            login(Request,user)
            return HttpResponseRedirect('/')

    return render(Request,"login.html")
 
 #logout 
def logoutPage(Request):
    logout(Request)
    return HttpResponseRedirect('/login/')
