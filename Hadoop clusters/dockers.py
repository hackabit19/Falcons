import subprocess
import os
subprocess.getoutput("yum install docker-ce")
subprocess.getoutput("systemctl start docker")
subprocess.getoutput("cd /root/docker_images/docker_images")
print("would u please tell me which os u want to launch centos or ubuntu ?")
print("enter ur choice...\n 1: centos\n2: ubuntu 14.04")
choice=int(input())
if choice==1:
	subprocess.getoutput("docker load -i centos-latest.tar")
	subprocess.getoutput("docker run -it centos:latest")
elif choice==2:
	subprocess.getoutput("docker load -i ubuntu-14.04.tar")
	subprocess.getoutput("docker run -it ubuntu:14.04")
else:
	print("you have entered wrong choice ...exiting")
	exit()
	
subprocess.getoutput("systemctl restart docker")
	 



