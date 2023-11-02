from django.urls import path

from login import views

urlpatterns =[
    path('',views.create_user,name ='register'),
    path('login',views.login,name ='login'),
    path('logout',views.logout,name ='logout'),
]