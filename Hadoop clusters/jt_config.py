import subprocess
import os


def jt():

    subprocess.getoutput("echo '192.168.43.{}	master.{}' >> /etc/hosts".format(ipm, k))
    subprocess.getoutput("hostnamectl set-hostname master.{}".format(k))
    subprocess.getoutput("echo '<?xml version="
    1.0
    "?><?xml-stylesheet type="
    text / xsl
    " href="
    configuration.xsl
    "?><configuration><property><name>fs.default.name</name><value>hdfs://master.{}:9001</value></property></configuration>' > /etc/hadoop/core-site.xml".format(
        k))
    subprocess.getoutput("hadoop namenode -Format")
    subprocess.getoutput("echo 'iptables -F' >> /etc/rc.d/rc.local")
    subprocess.getoutput("echo 'hadoop-daemon.sh start jobtracker' >> /etc/rc.d/rc.local")
    subprocess.getoutput("echo '<?xml version="
    1.0
    "?><?xml-stylesheet type="
    text / xsl
    " href="
    configuration.xsl
        "?><configuration><property><name>mapred.job.tracker</name><value>jt.{}:9002</value></property></configuration>' > /etc/hadoop/mapred-site.xml ".format(
            k))
    subprocess.getoutput("echo 'iptables -F' >> /etc/rc.d/rc.local")

jt()