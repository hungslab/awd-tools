import requests
for i in range(100):
	try:
		requests.get("http://192.168.103."+str(i)+":8080",timeout=0.1)
		print i
	except:
		print i,'bad url'
