#!/usr/bin/python
#coding=utf-8
import linecache
port=15000
f1=open('hosts.txt','r')
content1=f1.readlines()
f1.close()
f2=open('rmt.conf','r')
content2=f2.readlines()
f2.close()

for line1 in content1:
 f3=open('conf_mig/rmt_'+str(port)+'.conf','w+')
 for line2 in content2:
   a=line2.replace("SOURCE_REDIS",line1).replace("LISTEN_PORT",str(port))
   f3.writelines(a)
 f3.close
 port+=1
 
print "迁移配置文件生成完毕！"