#coding:utf-8
# @Time : 2020/9/4 下午5:35 
# @Author : wxm
# @File : urls.py 
# @Software: PyCharm


from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('login', views.login, name='login'),
    path('login_config', views.login_config, name='login_config'),
    path('register', views.register, name='register'),
    path('register_config', views.register_config, name='register_config'),
    path('ajax_login', views.ajax_login, name='ajax_login'),
    path('login_ajax_handle', views.login_ajax_handle, name='login_ajax_handle'),
    path('logout', views.logout, name='logout'),
    path('logout_flush', views.logout_flush, name='logout_flush'),
    path('url_reverse', views.url_reverse, name='url_reverse'),


]
