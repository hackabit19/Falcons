def java_i():
	import os
	import subprocess
	subprocess.getoutput("cp /root/Full/jdk-8u171-linux-x64.rpm /root")
	subprocess.getoutput('cd')
	#print("current version of installed java is:")
	#os.system('java -version')
	subprocess.getoutput('java -version &> java.txt')
	count = subprocess.getoutput("""grep -c "1.8.0_171" java.txt""")
	if count == 2:
		print("java version 1.8.0_171 is installed")
		subprocess.getoutput("exit()")
	else:
		print("installing the java...")
		os.system('rpm -Uvh jdk-8u171-linux-x64.rpm')
		
java_i()

