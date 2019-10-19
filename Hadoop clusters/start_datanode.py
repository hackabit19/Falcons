def start_datanode_server():
	import os
	import subprocess
	import time
	#from subprocess import call
	print("Stopping firewall....")
	subprocess.getoutput('iptables -F')
	print("First stopping any running datanode...")
	subprocess.getoutput("hadoop-daemon.sh stop datanode")
	print("Starting datanode....")
	os.system('hadoop-daemon.sh start datanode')
	time.sleep(2)
	print("starting tasktracker...")
	os.system('hadoop-daemon.sh start tasktracker')
	subprocess.getoutput("clear()")
	print("running jps")
	os.system('jps')
	os.system('exit()')


