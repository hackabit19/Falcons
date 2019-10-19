import subprocess
import os
#import install_hadoop
#import install_java
def client():
    # Client configuration
    ipc = int(input("enter the client ip : "))
    k = input("enter the client                                                               domain name : ")
    os.system("ssh-keygen")
    os.system("ssh-keyscan 192.168.43.{} > known_hosts".format(ipc))
    os.system("ssh-copy-id 192.168.43.{}".format(ipc))
    subprocess.getoutput("scp -r /root/Full 192.168.43.{}:/root".format(ipc))
    subprocess.getoutput("scp /root/Full/install_java.py 192.168.43.{}:/root".format(ipc))
    subprocess.getoutput("scp /root/Full/install_hadoop.py 192.168.43.{}:/root".format(ipc))
    subprocess.getoutput("scp /root/Full/yum_setup.py 192.168.43.{}:/root".format(ipc))
    subprocess.getoutput("echo '192.168.43.{}	client.{}' >> /etc/hosts".format(ipc, k))
    subprocess.getoutput("ssh 192.168.43.{} python36 install_java.py".format(ipc))
    subprocess.getoutput("ssh 192.168.43.{} python36 install_hadoop.py".format(ipc))
    subprocess.getoutput("ssh 192.168.43.{} python36 yum_setup.py".format(ipc))
    subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/core-site.xml""".format(ipc, k))
    subprocess.getoutput("""ssh 192.168.43.{} echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>mapred.job.tracker</name><value>jt.{}:9002</value></property></configuration>' > /etc/hadoop/mapred-site.xml """.format(ipc, k))
# subprocess.getoutput("exit()")