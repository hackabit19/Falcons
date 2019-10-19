import subprocess
def master():
    k = input("enter the cluster domain name : ")
    ipm = int(input("enter the master ip : "))

    # Master configuration
    subprocess.getoutput("cp /root/Full/install_java.py /root")
    subprocess.getoutput("cp /root/Full/install_hadoop.py /root")
    subprocess.getoutput("cp /root/Full/yum_setup.py /root")
    subprocess.getoutput("python36 /root/Full/install_java.py")
    subprocess.getoutput("python36 /root/Full/install_hadoop.py")
    subprocess.getoutput("python36 /root/Full/yum_setup.py")
    subprocess.getoutput("echo '192.168.43.{}	master.{}' >> /etc/hosts".format(ipm, k))
    subprocess.getoutput("hostnamectl set-hostname master.{}".format(k))
    subprocess.getoutput("""echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>dfs.name.dir</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/hdfs-site.xml""".format(k))
    subprocess.getoutput("mkdir /etc/hadoop//name")
    subprocess.getoutput( """echo '<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/core-site.xml""".format(k))
    subprocess.getoutput("hadoop namenode -Format")
    subprocess.getoutput("echo 'iptables -F' >> /etc/rc.d/rc.local")
    subprocess.getoutput("echo 'hadoop-daemon.sh start namenode' >> /etc/rc.d/rc.local")


master()