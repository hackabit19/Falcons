import subprocess
import os
#import install_hadoop
#import install_java

def cluster():
	
	k = input("enter the cluster domain name : ")
	n = int(input("enter no. of slaves in the cluster : "))
	ipm = int(input("enter the master ip : "))
	ipc = int(input("enter the client ip : "))
	ipj = int(input("enter the job tracker ip : ")) 
	l=[]

	#Master configuration
	subprocess.getoutput("cp /root/Full/install_java.py /root")
	subprocess.getoutput("cp /root/Full/install_hadoop.py")
	subprocess.getoutput("python36 /root/Full/install_java.py")
	subprocess.getoutput("python36 /root/Full/install_hadoop.py")
	subprocess.getoutput("echo '192.168.43.{}	master.{}' >> /etc/hosts".format(ipm, k))
	subprocess.getoutput("hostnamectl set-hostname master.{}".format(k))
	subprocess.getoutput("""echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>dfs.name.dir</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/hdfs-site.xml""".format(k))
	subprocess.getoutput("mkdir /etc/hadoop//name")
	subprocess.getoutput("""echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/core-site.xml""".format(k))
	subprocess.getoutput("hadoop namenode -Format")	
	subprocess.getoutput("echo 'iptables -F' >> /etc/rc.d/rc.local")
	subprocess.getoutput("echo 'hadoop-daemon.sh start namenode' >> /etc/rc.d/rc.local")
	subprocess.getoutput("hadoop-daemon.sh start namenode")
    
    
    
    

	#Client configuration
	os.system("ssh-keygen")
	os.system("ssh-keyscan 192.168.43.{} > known_hosts".format(ipc))
	os.system("ssh-copy-id 192.168.43.{}".format(ipc))
	subprocess.getoutput("scp -r /root/Full 192.168.43.{}:/root".format(ipc))
	subprocess.getoutput("scp /root/Full/install_java.py 192.168.43.{}:/root".format(ipc))
	subprocess.getoutput("scp /root/Full/install_hadoop.py 192.168.43.{}:/root".format(ipc))
	subprocess.getoutput("scp /root/Full/yum_setup.py 192.168.43.{}:/root".format(ipc))
	subprocess.getoutput("ssh 192.168.43.{} hostnamectl set-hostname client.{}".format(ipc, k))
	subprocess.getoutput("echo '192.168.43.{}	client.{}' >> /etc/hosts".format(ipm, k))
	subprocess.getoutput("ssh 192.168.43.{} python36 install_java.py".format(ipc))
	subprocess.getoutput("ssh 192.168.43.{} python36 install_hadoop.py".format(ipc))
	subprocess.getoutput("ssh 192.168.43.{} python36 yum_setup.py".format(ipc))
	subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/core-site.xml""".format(ipc, k))
	subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>mapred.job.tracker</name><value>jt.{}:9002</value></property></configuration>' > /etc/hadoop/mapred-site.xml """.format(ipc, k))
	#subprocess.getoutput("exit()")
	
	#Job tracker configuration
	subprocess.getoutput("ssh-keyscan 192.168.43.{} > known_hosts".format(ipj))
	subprocess.getoutput("ssh-copy-id 192.168.43.{}".format(ipj))
	subprocess.getoutput("scp -r /root/Full 192.168.43.{}:/root ".format(ipj))
	subprocess.getoutput("scp  /root/Full/install_java.py 192.168.43.{}:/root".format(ipj))
	subprocess.getoutput("scp  /root/Full/install_hadoop.py 192.168.43.{}:/root".format(ipj))
	subprocess.getoutput("scp /root/Full/yum_setup.py 192.168.43.{}:/root".format(ipj))
	subprocess.getoutput("echo '192.168.43.{}	jt.{}' >> /etc/hosts".format(ipm, k))
	subprocess.getoutput("ssh 192.168.43.{} hostnamectl set-hostname jt.{}".format(ipj, k))
	subprocess.getoutput("ssh 192.168.43.{} python36 install_java.py".format(ipj))
	subprocess.getoutput("ssh 192.168.43.{} python36 instll_hadoop.py".format(ipj))
	subprocess.getoutput("ssh 192.168.43.{} python36 yum_setup.py".format(ipj))
	subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/core-site.xml""".format(ipj, k))
	subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>mapred.job.tracker</name><value>jt.{}:9002</value></property></configuration>' > /etc/hadoop/mapred-site.xml""".format(ipj, k))
	subprocess.getoutput("""ssh 192.168.43.{} echo 'hadoop-daemon.sh start jobtracker' >> /etc/rc.d/rc.local""".format(ipj))
	subprocess.getoutput("ssh 192.168.43.{} hadoop-daemon.sh start jobtracker".format(ipj))
	
	#Slaves configuration (Both datanodes and tast trackers)
	print("enter the ip of all slaves  :")
	for i in range(n):
		ips = int(input())
		l.append(ips)
	


	count = 1
	for j in l:
		subprocess.getoutput("ssh-keyscan 192.168.43.{} > known_hosts".format(j))
		subprocess.getoutput("ssh-copy-id 192.168.43.{}".format(j))
		subprocess.getoutput("scp -r /root/Full 192.168.43.{}:/root".format(j))
		subprocess.getoutput("echo '192.168.43.{}	slave{}.{}' >> /etc/hosts".format(j, count, k))
		#to login to remote host terminal once.
		subprocess.getoutput("scp  /root/Full/install_java.py 192.168.43.{}:/root".format(j))
		subprocess.getoutput("scp  /root/Full/install_hadoop.py 192.168.43.{}:/root".format(j))
		subprocess.getoutput("scp /root/Full/yum_setup.py 192.168.43.{}:/root".format(j))
		subprocess.getoutput("ssh 192.168.43.{} python36 install_java.py".format(j)) 
		subprocess.getoutput("ssh 192.168.43.{} python36 instll_hadoop.py".format(j))
		subprocess.getoutput("ssh 192.168.43.{} python36 yum_setup.py".format(j))
		subprocess.getoutput("ssh 192.168.43.{} hostnamectl set-hostname slave{}.{}".format(j, count, k))
		subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>dfs.data.dir</name><value>/data</value></property></configuration>' > /etc/hadoop/hdfs-site.xml""".format(j, k))
		subprocess.getoutput("ssh 192.168.168.43.{} mkdir /etc/hadoop//data".format(j))
		subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/core-site.xml""".format(j,k))
		subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>mapred.job.tracker</name><value>jt.{}:9002</value></property></configuration>' > /etc/hadoop/mapred-site.xml """.format(j,k))
		subprocess.getoutput("ssh 192.168.43.{} echo 'iptables -F' >> /etc/rc.d/rc.local".format(j))
		subprocess.getoutput("ssh 192.168.43.{} echo 'hadoop-daemon.sh start datanode' >> /etc/rc.d/rc.local".format(j))
		subprocess.getoutput("ssh 192.168.43.{} echo 'hadoop-daemon.sh start tasktacker' >> /etc/rc.d/rc.local".format(j))
		subprocess.getoutput("ssh 192.168.43.{} hadoop-daemon.sh start datanode".format(j)) 
		subprocess.getoutput("ssh 192.168.43.{} hadoop-daemon.sh start tasktracker".format(j))

	count = count+1

	l1=l[:]	
	l1.append(ipc)
	l1.append(ipj)
	for t in l1:
		subprocess.getoutput("scp /etc/hosts 192.168.43.{}:/etc/hosts".format(t))	
		
cluster()		




