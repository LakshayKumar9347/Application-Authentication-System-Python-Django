from django.contrib import admin
from django.urls import path,include
from home import views
# from home.views import 
urlpatterns = [
    path('',views.index,name='index.html'),
    path('login',views.loginUser,name='login.html'),
    path('logout',views.logoutUser,name='logout.html'),

]
