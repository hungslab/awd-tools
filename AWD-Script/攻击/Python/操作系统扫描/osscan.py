import nmap
import optparse

def osscan(host):
	scanner = nmap.PortScanner()
	results = scanner.scan(hosts=host,arguments='-O')
	res = results['scan'].values()
	print res[0]['osmatch'][0]['name']

def main():
	parser=optparse.OptionParser('usage%prog'+'-H <target>')  #�����е�����Ϊ������Ϣ,"%prog"Ϊ�ļ���
	parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
	(options,args) = parser.parse_args()
	host=options.tgtHost   #��õ�host��dest��ֵ
	if host==None:
		print parser.usage   #��û�д���ֵʱ��ʾ����
		exit(0)
	osscan(host)

if __name__ == '__main__':
	main()
