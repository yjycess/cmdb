# coding:utf-8

from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.acc_login,name='login'),
    url(r'^index/', views.index, name='index'),
    #url(r'^login/', views.acc_login,name='login'),
    url(r'^logout/', views.acc_logout,name='logout'),
    url(r'^operate_info/', views.operate_info, name='operate_info'),
    url(r'^operate_info_add/', views.operate_info_add, name='operate_info_add'),
    url(r'^operate_room/', views.operate_room, name='operate_room'),
    url(r'^operate_cmd/', views.operate_cmd, name='operate_cmd'),
    url(r'^operate_file/', views.operate_file, name='operate_file'),
]
