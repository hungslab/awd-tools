a=`head -c 500 /dev/urandom | tr -dc a-z |head -c 5`
useradd $a
echo "$a:123456" | chpasswd

