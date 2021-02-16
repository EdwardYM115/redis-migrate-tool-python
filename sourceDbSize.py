#!/usr/bin/python
#coding=utf-8
import linecache
import os
import commands
f=open('hosts.txt','r')
count=len(f.readlines())
f.close()
f=open('hosts.txt','r')
i=0
sumdbsize=0
while i < count:
 line=f.readline()
 a=line.split(':')
 print('../redis-cli -h '+str(a[0]).rstrip()+' -p '+str(a[1]).rstrip()+' -a PASSWORD DBSIZE')
 b=commands.getstatusoutput('../redis-cli -h '+str(a[0]).rstrip()+' -p '+str(a[1]).rstrip()+' -a PASSWORD DBSIZE')
 dbsize=b[1]
 sumdbsize=sumdbsize+int(dbsize)
 print(str(a[0]).rstrip()+':'+str(a[1]).rstrip()+'='+str(dbsize).rstrip())
 i+=1
print('Total DBSize:'+str(sumdbsize).rstrip())
f.close()