# coding:utf-8

from django.contrib import admin
import models

class Device_Admin(admin.ModelAdmin): #自定义，让admin后台显示字段
    list_display = ('id','ip', 'operate_room', 'device_brand','operate_room','operate_room_Cabinet','os_system','up_time','describtion')

class Operate_Room_Admin(admin.ModelAdmin):
    list_display = ('id','name', 'address')

class Virt_ip_Admin(admin.ModelAdmin):
    list_display = ('id','virt_ip', 'virsh_name','su_host_ip')

admin.site.register(models.Device,Device_Admin)
admin.site.register(models.Operate_Room,Operate_Room_Admin)
admin.site.register(models.Virt_ip,Virt_ip_Admin)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)

