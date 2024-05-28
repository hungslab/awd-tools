for Dir in $(ls /var/www/PanYun | grep .php)
do
	name=`head -c 500 /dev/urandom | tr -dc a-z |head -c 7`
	mv /var/www/PanYun/$Dir /var/www/PanYun/$name.php
done
