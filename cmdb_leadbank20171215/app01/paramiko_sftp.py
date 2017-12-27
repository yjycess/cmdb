__author__ = 'lewis'
# coding:utf-8

import paramiko
import os,time

def SshClient(hostip,password,cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostip, port=59322, username='root', password=password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    # print stdout.read()
    commands = stdout.read()
    # print commands
    ssh.close()
    return commands

def UploadFile(upload_host,inp_upload_path,new_file_path,inp_upload_file_new):
    hostname = upload_host
    port = 59322
    username = 'root'
    password = 'lead1234#'
    print ('-+: ',new_file_path,inp_upload_path,inp_upload_file_new)

    timeNow = time.strftime("%Y%m%d%H%M%S")
    local_dir = new_file_path
    remote_dir = inp_upload_path+"/"+ timeNow + inp_upload_file_new
    print ("++local_dir",local_dir)
    print ("++remote_dir: ",remote_dir)
    #local_dir = '/root/lotterya-2017-03-0519.tar.gz'  # 本地文件
    #remote_dir = '/home/lotterya-2017-03-0519.tar.gz'  # 远程服务器目录

    try:
        t = paramiko.Transport((hostname,port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_dir,remote_dir)
        print ("+++++++++++ success +++++++++++++")
        t.close()
        return "Success"
    except Exception,e:
        print ("upload file is error ",e)

#if __name__ == '__main__':
#    UploadFile("10.1.1.101","/opt","/root/lotterya-2017.tar.gz","lotterya.tar.gz")
