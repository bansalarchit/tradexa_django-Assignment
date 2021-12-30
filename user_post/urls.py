from django.urls import path, include

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addtext', views.Post_detail, name='Post_detail')

    
]

