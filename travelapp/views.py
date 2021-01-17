from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from .forms import register1


# Create your views here.
def tour(request):

    trv= travell.objects.all()
    blg = blog.objects.all()
    return render(request,'index.html',{'trv':trv,'blg':blg})

def register2(request):
    form = register1(request.POST, request.FILES)
    if request.method == 'POST':
            first_name =request.POST['name']
            last_name =request.POST['lname']
            email =request.POST['email']
            user_name =request.POST['username']
            password =request.POST['password']
            password1 =request.POST['password1']
            dob =request.POST['dob']
            national =request.POST['nationality']
            gender =request.POST['gender']
            phone =request.POST['mobile']
            address =request.POST['address']
            image = request.POST['image']
            print(gender,dob,national,)
            print(image)
            user = User(username=user_name,password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()
            user.set_password(password)
            user.save()
            user=User.objects.get(username=user_name)
            print(user)


            try:
                print(form.is_valid())
                if form.is_valid():
                    form.save()
                return redirect('/register/')
            except Exception as e:
                print(e)
            # reg=register(dob=dob,mobile=phone,gender=gender,address=address,image=image,nationality=national,username=user_name)
            # reg.save()
            print('user created')
            return redirect('/')

    return render(request,'register.html' ,{'form': form})

def login2(request):
    if request.method == "POST":
        user_name =request.POST['user']
        password =request.POST['password']
        user=User.objects.get(username=user_name)
        # user =authenticate(username=user_name,password=password)
        print(user.check_password(password))
        if user.check_password(password):
        # if user is not None:
        #     auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid username or password')
            return redirect("login")

    return render(request,'login.html')