#!/usr/bin/python
#coding=utf-8
import os
import commands
j = commands.getstatusoutput('netstat -antlp|grep 127.0.0.1:1500*|wc -l')
i=0
cmd = raw_input("请确认是否要结束迁移进程。确认请输入y，取消请输入其它任意字符：")
if ( cmd == 'y' ):
 while i < int(j[1]):
  os.system('/redis-cli -p '+str(i+15000)+' shutdown')
  os.system('sleep 2')
  i+=1
 procnum = commands.getstatusoutput('ps -ef|grep redis-migrate-tool|wc -l')
 if ( procnum[1] == '2' ):
  print "迁移进程已结束"
 else:
  print "迁移进程未全部结束，请手动结束redis-migrate-tool进程"