from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Post
from product.models import Product
from .forms import PostForm


def home(request):
    return render(request, 'home.html') 

#def post(request):
 #   return render(request, 'postform.html') 

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password_confirm']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken, try again')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken, try again')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                user.save();
        else:
            messages.info(request,'password is not same, try again')
            return redirect('register')

        return redirect('login')





    else:
        return render(request, 'register.html') 

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('addproduct/logedin')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'log_in.html') 

def logout (request):
    auth.logout(request)
    return render(request, 'home.html')

def Post_detail(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        print (form.errors)  
        if form.is_valid(): 
            obj = form.save(commit = False)
            obj.user=request.user;
            obj.save()
            form = PostForm()
            #messages.success(request, "Successfully created")
            posts = Post.objects.all()
            products =Product.objects.all()
            return render(request, 'home.html',{'products':products, 'posts' : posts})
        else:
            
            print('tell')
            return render(request, 'home.html')

    else:      
        return render(request, 'formtext.html', {'form':form})


