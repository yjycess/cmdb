# coding:utf-8

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from app01 import models
from app01.forms import Operate_File,handle_upload_file
from app01.paramiko_sftp import SshClient,UploadFile
from app01.open_file import Openfile,Openinfoadd
import paramiko,time

def acc_login(request):
    #print request.POST
    err_msg = ''
    if request.method == "POST":
        #print ('------123')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)  #第一步验证用户名密码
        #print ('--> ',user)
        if user is not None:
            login(request,user)  #第二步登录，并生成session
            return render(request,"operate_info.html")
        else:
            err_msg = "username and password error"
    return render(request,'login.html',{'err_msg':err_msg})

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect("/")  #跳转到首页

def index(request):
    device = models.Device.objects.all()
    return render(request,'index.html',{'device':device})

def operate_info(request):
    obj_list = models.Device.objects.all()
    obj_virt_ip = models.Virt_ip.objects.all()
    #print request.path
    if request.method == "POST":
        data_list_ip =request.POST.get('su_host_ip_id')
        print("---> ",data_list_ip)
    return render(request,'operate_info.html' ,{'obj_list':obj_list,'obj_virt_ip':obj_virt_ip})

def operate_info_add(request):
    err_msg = ""
    rig_msg = ""
    obj_list = models.Device.objects.all()
    obj_room = models.Operate_Room.objects.all()
    if request.method == "POST":
        #print request.POST['disk']
        inp_obj1 = request.POST.get("su_ip")
        inp_obj2 = request.POST.get("operate_room")
        inp_obj3 = request.POST.get("operate_room_Cabinet")
        inp_obj4 = request.POST.get("device_brand")
        inp_obj5 = request.POST.get("cpu")
        inp_obj6 = request.POST.get("memory")
        inp_obj7 = request.POST.get("disk")
        inp_obj8 = request.POST.get("sn")
        inp_obj9 = request.POST.get("os_system")
        inp_obj10 = request.POST.get("describtion")
        print (inp_obj1, inp_obj2, inp_obj3, inp_obj4, inp_obj5, inp_obj6, inp_obj7, inp_obj8, inp_obj9, inp_obj10)
        if request.POST is not None:
            dic = {'ip': request.POST['su_ip'], 'operate_room_id': request.POST['operate_room'],'operate_room_Cabinet': request.POST['operate_room_Cabinet'],
                   'device_brand': request.POST['device_brand'],'cpu': request.POST['cpu'],'memory': request.POST['memory']
                , 'disk': request.POST['disk'], 'sn': request.POST['sn'], 'os_system': request.POST['os_system']
                , 'describtion': request.POST['describtion']}

            username_cmd = request.user.userprofile.name    #获取当前登录的用户名
            openinfoadd = Openinfoadd(username_cmd,inp_obj1)  #将info_add添加到input_info_add.log文件里
            print ("->openinfoadd: ",openinfoadd)

            models.Device.objects.create(**dic)
            rig_msg = "添加成功..."

            return render(request,'operate_info_add.html',{'rig_msg':rig_msg})
        else:
            err_msg = "错误，所有信息必填，请重新填写..."
    return render(request,'operate_info_add.html',{'obj_list':obj_list,'obj_room':obj_room,'err_msg':err_msg})

def operate_room(request):
    obj_room = models.Operate_Room.objects.all()

    #print request.POST
    err_msg = ''
    if request.method == "POST":
        room_name = request.POST.get('operate_room_name')
        address = request.POST.get('operate_room_address')
        print (type(room_name),room_name.encode("utf-8"))
        if len(room_name) != 0 :
            print ("--2 ", room_name, address)
            dic = {'name': room_name, 'address': address}
            models.Operate_Room.objects.create(**dic)
        else:
            err_msg = "错误，机房名和地址不能空，请重新填写..."
    return render(request, 'operate_room.html',{'obj_room':obj_room,'err_msg':err_msg})

def operate_cmd(request):
    #print (request.POST)
    if request.method == 'POST':
        inp_obj_f1 = request.POST.get('f1')
        inp_obj_f3 = request.POST.get('f3')
        inp_obj_f4 = request.POST.get('f4')
        hostip = inp_obj_f1
        password = inp_obj_f3
        cmd = inp_obj_f4
        #print (hostip,password,cmd)

        username_cmd = request.user.userprofile.name    #获取当前登录的用户名
        #print ('-+> :',username_cmd)

        openfile_obj = Openfile(username_cmd,hostip,cmd)
        print ("->:openfile",openfile_obj)

        commands = SshClient(hostip,password,cmd)

        return render(request, "operate_cmd.html", {'commands': commands})
    return  render(request, 'operate_cmd.html')  #读取html文件返回给用户

def operate_file(request):   #处理上传文件，也可以是上传图片
    if request.method == "POST":
        #print ("++>: ",request.POST)
        #print ("==>: ",request.FILES)  # request.FILES获取文件
        inp_upload_host = request.POST.get('upload_host')
        inp_upload_path = request.POST.get('upload_path')
        inp_upload_file = request.POST.get('upload_file')
        inp_upload_file_new = request.POST.get('upload_file_new')
        print ("host and path and file and file_new: ",inp_upload_host,inp_upload_path,inp_upload_file,inp_upload_file_new)

        form = Operate_File(request.POST, request.FILES)  #  form表单验证来获取数据和文件
        #print ("-->form: ",form)
        #print ("-->is_valid: ",form.is_valid())
        if form.is_valid():
            #print ("-->form data:", form.cleaned_data)
            form_data = form.cleaned_data
            form_data['upload_name'] = request.user.userprofile.name # 存上传文件的用户名
            new_file_path = handle_upload_file(request, request.FILES['upload_file'])  # 获取发帖页面上传的图片名字
            print ("->new_file_path: ",new_file_path)

            models.Operate_File.objects.create(**form_data)
            Uploadfile = UploadFile(inp_upload_host,inp_upload_path,new_file_path,inp_upload_file_new)    #调用paramiko_sftp.py
            print ("==uploadfile: ",Uploadfile)
 
            return render(request, 'operate_file.html',{"Uploadfile":Uploadfile})
        else:
            print ("-->err:", form.errors)
    return render(request, 'operate_file.html')
