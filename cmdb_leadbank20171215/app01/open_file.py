__author__ = 'lewis'
# coding:utf-8

from app01 import models
import time

def Openfile(username_cmd,hostip,cmd):   #用于存储执行过的shell命令
    f = open('input_cmd.log', 'ab')
    Timenow = time.strftime("%Y%m%d%H%M")
    log_cmd = username_cmd + ',' + Timenow + ',' + hostip + ',' + cmd + ',' + '\n'
    # print ('--> : ', log_cmd)
    models.Log_cmd.objects.create(cmd=log_cmd)  # 写到数据库log_cmd表中
    f.writelines(log_cmd)  # 写到input_cmd.log文件里
    f.close()
    return "input shell cmd success..."

def Openinfoadd(username_cmd,hostip):
    f = open('input_info_add.log', 'ab')
    Timenow = time.strftime("%Y%m%d%H%M")
    host_ip_obj = username_cmd + ',' + Timenow + ',' + 'add' + ',' + hostip + ',' + '\n'
    # print ('--> : ',     host_ip_obj)
    f.writelines(host_ip_obj)  # 写到input_cmd.log文件里
    f.close()
    return "operate info add success..."
