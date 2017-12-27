# coding:utf-8

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User   #django自带论证表

class Operate_Room(models.Model):
    name = models.CharField(max_length=30,unique=True,verbose_name=u'机房名')  #唯一
    address = models.CharField(max_length=255,verbose_name=u'机房地址')
    class Meta:         # 此类的意思是在admin表中显示中文名
        verbose_name = '机房'
        verbose_name_plural = "机房"
    def __unicode__(self):       # 用于在前端页面显示中文名
        return self.name

class Operate_File(models.Model):    #用于记录上传文件的信息
    upload_name = models.CharField(max_length=64)
    upload_host = models.CharField(max_length=255)
    upload_path = models.CharField(max_length=64)
    upload_file = models.CharField(max_length=255)

class Device(models.Model):    #设备表
    ip = models.GenericIPAddressField(unique=True,null=True,verbose_name=u'IP地址')
    operate_room = models.ForeignKey('Operate_Room',verbose_name=u'机房名')   #机房
    operate_room_Cabinet = models.CharField(max_length=32,verbose_name=u'机柜')
    device_brand = models.CharField(max_length=20,verbose_name=u'设备品牌')   #设备品牌
    cpu = models.IntegerField(null=True)
    memory = models.IntegerField(null=True)
    disk = models.IntegerField(null=True)
    sn = models.CharField(max_length=40,unique=True,null=True)
    up_time = models.DateTimeField(auto_now=True)
    os_system = models.CharField(max_length=100,blank=True,null=True,verbose_name=u'操作系统')
    describtion = models.CharField(max_length=100,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):       # 用于在前端页面显示中文名
        return self.ip

class Virt_ip(models.Model):     #虚拟IP
    virt_ip = models.GenericIPAddressField(max_length=32,unique=True,null=True,verbose_name=u'虚拟IP')
    virsh_name = models.CharField(max_length=64,verbose_name=u'虚拟机名')
    su_host_ip = models.ForeignKey('Device',verbose_name=u'宿主机IP')
    def __unicode__(self):       # 用于在前端页面显示中文名
        return self.virt_ip

class UserProfile(models.Model):  #用户表
    user = models.OneToOneField(User)  # django自带的论证表
    name = models.CharField(max_length=32,verbose_name=u'用户名称')
    group = models.ManyToManyField("UserGroup",verbose_name=u'用户组名')
    def __unicode__(self):  # 默认返回值
        return self.name

class UserGroup(models.Model):  #用户组表
    name = models.CharField(max_length=32,unique=True,verbose_name=u'用户组名')
    def __unicode__(self):  # 默认返回值
        return self.name

class Log_cmd(models.Model):  #存operate_cmd.html页面执行的命令
    cmd = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True, verbose_name=u'执行命令时间')
    def __unicode__(self):
        return self.cmd
