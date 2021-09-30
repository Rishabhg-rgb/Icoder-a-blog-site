from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns =[
    path('',views.bloghome , name='bloghome'),
    path('<str:slug>',views.blogpost,name='blogpost'),

]