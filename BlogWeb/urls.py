"""
URL configuration for BlogWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main_v
from user import views as user_v
from blog import views as blog_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , main_v.index , name='index'),
    path('contactus/' , main_v.contactus , name='contactus'),
    path('signup/' , user_v.signup , name='signup'),
    path('login/' , user_v.loginReq , name='loginReq' ),
    path('logout/', user_v.logoutReq , name='logoutReq'),
    path('post/<slug:slug>' , blog_v.blogpost , name='blogpost'),
    path('createpost/' , blog_v.createPost , name='createPost'),
    path('yourpost/' , blog_v.yourPost , name='yourPost'),
    path('editpost/<slug:postSlug>' , blog_v.editPost , name='editPost'),
    path('deletepost/<slug:delSlug>' , blog_v.deletePost , name='delelePost'),
    path('explore/' , main_v.explore , name='explore' )
]
