def start_namenode_server():
	import os
	import subprocess
	import time
	print("Stopping firewall....")
	subprocess.getoutput('iptables -F')
	print("First stopping any running namenode...")
	subprocess.getoutput("hadoop-daemon.sh stop namenode")
	print("Starting namenode....")
	os.system('hadoop-daemon.sh start namenode')
	time.sleep(2)
	subprocess.getoutput('clear')
	print("running jps")
	os.system('jps')
	os.system('exit()')


