from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
from django.contrib.auth import logout ,authenticate , login

# admin user admin password
# lucky passwords is radheradhe 

# Create your views here.
def index(request):
  # print(request.user)
  if request.user.is_anonymous:
    return redirect("/login")
  return render(request,'index.html')

def loginUser(request):
  if request.method=="POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    # print(username,password)
    #  check if user has entered correct credentials
    user = authenticate(username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
      login(request,user)
      return redirect("/")  
        # No backend authenticated the credentials
    else:
      return render(request,'login.html')

  return render(request,'login.html')

def logoutUser(request):
  logout(request)
  return  redirect("/login")



 #  username = request.POST.get('username')
  # password = request.POST.get('password')
  #  user = authenticate(username='john', password='secret')
  # if user is not None:
  #     # A backend authenticated the credentials
  #     return redirect('/')  
  #     # No backend authenticated the credentials
  # else:
  #     return redirect('/login')
  #     #check wheter the user is authenticated or not