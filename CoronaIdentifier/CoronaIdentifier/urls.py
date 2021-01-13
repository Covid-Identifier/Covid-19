"""CoronaIdentifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Authentication.views import Signup,Login,Logout,Change_Password
from AboutUser.views import Test,Visualization,Profile,Home,profileEdit

pk = ''
def PK(request):
    global pk
    current_user = request.user
    pk=current_user.id



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('signup/',Signup,name='signup'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('change_password/',Change_Password,name='changepassword'),
    path('test/', Test, name='test'),
    path('visualization/', Visualization, name='visualization'),
    path('profile/', Profile, name='profile'),
    path('myresult/<int:pk>/',profileEdit.as_view(),name='resultEdit'),

]
