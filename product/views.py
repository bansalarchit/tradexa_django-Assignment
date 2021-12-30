from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
from user_post.models import Post
from django.contrib import messages
# Create your views here.

def add (request) :
    return render(request,'postform.html') 
  
def Product_detail(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
          
        if form.is_valid():
              
            obj = form.save(commit = False)
           # obj.user = request.user
            obj.save();
            form = ProductForm()
            #messages.success(request, "Successfully created")
            products = Product.objects.all()
            posts= Post.objects.all()
            return render(request, 'home.html',{'products' : products, 'posts' : posts})

    else:      
        return render(request, 'form.html', {'form':form})

