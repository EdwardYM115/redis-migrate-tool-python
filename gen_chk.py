#!/usr/bin/python
#coding=utf-8
import linecache
port=15000
f1=open('hosts.txt','r')
content1=f1.readlines()
f1.close()
f2=open('rmt.conf','r')
content2=f2.readlines()
count=len(content2)
f2.close()

for line1 in content1:
 i=1
 f3=open('conf_chk/rmt_'+str(port)+'.conf','w+')
 for line2 in content2:
  a=line2.replace("SOURCE_REDIS",line1.rstrip())
  if (i < count):
   f3.writelines(a)
   i+=1
  else:
   continue
 f3.close()
 port+=1
 
print "校验配置文件生成完毕！"