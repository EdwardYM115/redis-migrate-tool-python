#!/usr/bin/python
#coding=utf-8
import os
import commands
import linecache
f=open('hosts.txt','r')
count=len(f.readlines())
f.close()
i=0
procnum=commands.getstatusoutput('ps -ef|grep redis-migrate-tool|wc -l')
if procnum[1] == '2':
 while (i < count):
  j=15000+i
  os.system('./redis-migrate-tool'+' '+'-c'+' '+'./conf_mig/rmt_'+str(j)+'.conf'+' '+'-o'+' '+'log/'+str(j)+'.log'+' '+'-d')
  os.system('sleep 5')
  i+=1
 procnum=commands.getstatusoutput('ps -ef|grep redis-migrate-tool|wc -l')
 if procnum[1] == str(int(count)+2):
  print "迁移进程已启动"
 else:
  print "迁移进程未启动或未全部启动，请确认"
  print ('应启动进程数：'+str(count))
  print ('已启动进程数：'+str(int(pronum[1])-2))
else:
 print "系统中已有迁移进程存在，不可重复启动"