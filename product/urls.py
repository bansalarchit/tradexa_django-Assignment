from django.urls import path
  
from . import views
urlpatterns = [
      
    path('/', views.Product_detail, name='Product_detail'),
    path('/logedin', views.add, name='add')
    

]