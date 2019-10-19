import subprocess


def yum():

	#we can check if the iso dvd is available 	
	subprocess.getoutput("mkdir /dvd")
	subprocess.getoutput("mount  /dev/cdrom  /dvd")
	subprocess.getoutput("echo '[mydvd]' >> /etc/yum.conf")
	subprocess.getoutput("echo 'baseurl=file:///dvd' >> /etc/yum.conf")
	subprocess.getoutput("echo 'gpgcheck=0' >> /etc/yum.conf")

	#check if yum configuraton is successful
	#check if last few chars of file (if 0 -> not configured)	
	#subprocess.getoutput("yum repolist > new_file.txt")
	
	subprocess.getoutput("echo 'mount  /dev/cdrom  /dvd'  >> /etc/rc.d/rc.local")
	subprocess.getoutput("chmod  +x  /etc/rc.d/rc.local")
	




yum()
