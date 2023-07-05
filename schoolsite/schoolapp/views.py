from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request,"index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('pre_form')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if cpassword == password:

            if User.objects.filter(username =username).exists():
                messages.info(request,"username taken")
                return redirect('signup')
            if User.objects.filter(email =email).exists():
                messages.info(request,"email taken")
                return redirect('signup')
            else:

                user = User.objects.create_user(username =username,email=email, password= password  )
                user.save();
                return redirect('login_view')

        else:
            messages.info(request,"password dont match")
            return redirect('signup')

        return redirect('/')


    return render(request,"signup.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def pre_form(request):
    return render(request,"preform.html")

def form(request):
    return render(request,"form.html")