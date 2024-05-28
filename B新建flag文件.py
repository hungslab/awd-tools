#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import string
import os

def visitDir(path):
    if not os.path.isdir(path):
        print('Error: "', path, '" is not a directory or does not exist.')
        return
    else:
        global x
        try:
            for lists in os.listdir(path):
                sub_path = os.path.join(path, lists)
                x += 1
        except:
            pass


if __name__ == '__main__':
    x = 0
    visitDir('/root')
    print('Total Permission Files: ', x)
if x<=200:
	ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
	ran_str2 = ''.join(random.sample(string.ascii_letters + string.digits, 16))
	file = open('/root/flaginfo'+ran_str+'.txt','w')
	file.write(ran_str2)
