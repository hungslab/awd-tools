#!/usr/bin/python
import sys
for i in range(100):
	try:
		r=sys.argv[i]
		a=int(r)
		print chr(a),
	except:
		continue
	
