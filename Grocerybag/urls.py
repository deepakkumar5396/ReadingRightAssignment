from django.contrib import admin
from django.urls import path,include
from Grocerybag.views import *
urlpatterns = [
    path('',home,name='home'),
    path('user_login',user_login,name='user_login'),
    path('user_signup',user_signup,name='user_signup'),
    path('Logout', Logout, name='Logout'),
    path('user_home',user_home,name='user_home'),
    path('add',add,name='add'),
    path('update',update,name='update'),
    path('index',index,name='index'),



 ]