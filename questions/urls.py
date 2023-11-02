from django.urls import path

from questions import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post', views.create_post, name='create_post'),
    path('post_answers/<int:id>', views.post_answers, name='post_answers'),
    path('like_answer/<int:id>',views.like_answer,name ='like_answer')

]
