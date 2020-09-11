# coding:utf-8
# @Time : 2020/9/3 下午2:44 
# @Author : wxm
# @File : urls.py 
# @Software: PyCharm

from django.contrib import admin
from django.urls import path
from booktest import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('showbooks', views.show_books, name='show_books'),
    path('showheros/<int:bid>', views.show_heros, name='show_heros'),
    path('book/add', views.book_add, name='book_add'),
    path('book/delete/<int:bid>', views.book_delete, name='book_delete'),
    path('showareas/<int:bid>', views.showareas, name='showareas'),
    path('allarea/<int:pindex>', views.allarea, name='allarea'),
    path('upload_handle', views.upload_handle, name='upload_handle'),
    path('upload_pic', views.upload_pic, name='upload_pic'),
]
