import os
import subprocess
def hadoop():
    subprocess.getoutput("cp /root/Full/hadoop-1.2.1-1.x86_64.rpm /root")
    subprocess.getoutput('hadoop version > hadoop.txt')
    count=subprocess.getoutput("""grep -c "1.2.1" x.txt""")
    if count==2:
        print("hadooop version 1.2.1 is installed")
        subprocess.getoutput('exit()')
    else:
        #print("enter the path for hadoop rpm")
        #path=input()
        #subprocess.getoutput('cd path')
        print("installing hadoop version 1.2.1....")
        os.system('rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force')
        os.system('hadoop version')
hadoop()