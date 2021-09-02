from django.urls import path, re_path
from . import views

app_name = 'account'
URLPattern = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
