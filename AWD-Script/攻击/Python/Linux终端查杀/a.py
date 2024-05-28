import os,time
i=1
while True:
	i+=1
	os.system('w')
	os.system('pkill -kill -t pts/3')
	os.system('pkill -kill -t pts/4')
	os.system('pkill -kill -t pts/5')
	os.system('pkill -kill -t pts/6')
	os.system('pkill -kill -t pts/7')
	os.system('pkill -kill -t pts/8')
	os.system('pkill -kill -t pts/9')
	time.sleep(1)
