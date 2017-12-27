#  coding:utf-8

from django import forms
import os,time
# forms表单验证

class Operate_File(forms.Form):
    upload_host = forms.CharField(max_length=255,min_length=5)
    upload_path = forms.CharField(max_length=255,min_length=2)
    upload_file = forms.FileField()

def handle_upload_file(request,f):  #用于处理发帖页面上传的文件,reques是用于获取前端输入的数据

    new_name = time.strftime("%Y%m%d%H%M%S") + f.name
    print ("-->name and new_name :", f.name,new_name)
    base_file_upload_path = 'static/files'    #自定义图片上传目录
    user_path = "%s/%s"%(base_file_upload_path,request.user.userprofile.id)  #谁上传的图片就在目录里创建用户ID的文件夹
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open("%s/%s"%(user_path,new_name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    new_name_obj = "/cmdb_leadbank20171215/static/files/%s/%s"%(request.user.userprofile.id,new_name)
    return new_name_obj
