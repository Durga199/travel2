from django.urls import path
from . import views

urlpatterns =[
    path('',views.tour,name='tour'),
    path('register/',views.register2,name='register'),
    path('login/',views.login2,name='login')
   
]
