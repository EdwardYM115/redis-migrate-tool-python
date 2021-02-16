#!/usr/bin/python
#coding=utf-8
import os
import linecache
f=open("info.txt","r")
content=f.readlines()
f.close()
i=1
for line in content:
 if i==2:
  JDCAUTH=line
 if i==6:
  JDCURL=line
 i+=1
os.system('python sourceDbSize.py > dbsize.out')
f=open("dbsize.out","r")
content=f.readlines()
f.close()
print "源端和目的端key数量信息："
print "---------JIMDB-----------"
print content[-1]
print "----------JDC------------"
os.system('redis-cli -h '+str(JDCURL).rstrip()+' -a '+str(JDCAUTH).rstrip()+' info|sed -n '$p'')