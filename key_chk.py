#!/usr/bin/python
#coding=utf-8
import linecache
import os
import math
cmd=raw_input("请确认迁移源实例有从库且当前连接的是从库。确认请输入y，如无从库请输入其它任意字符退出，进行手动校验：")
if ( cmd == 'y' ):
 os.system('python sourceDbSize.py > dbsize.out')
 f=open("hosts.txt","r")
 procnum=len(f.readlines())
 f.close()
 percent=raw_input("请设置校验key数量占key总数量的除比，建议设置为10的n次幂：")
 while (percent.isdigit() == False or int(percent) == 0):
  percent=raw_input("非法输入值！请输入非零数字：")
 f=open("dbsize.out","r")
 i=0
 while i < procnum:
  line=f.readline() 
  a=line.split( )
  b=a[3]
  print b
  j=int(b)//int(percent)
  print j
  k=i+15000
  i+=1
  os.system('echo "分片'+str(i)+'：" >> checksum.out')
  os.system('./redis-migrate-tool -c conf_check/rmt_'+str(k)+'.conf -o log/check'+str(i)+' -C "redis_check '+str(j)+'" >> checksum.out')
 f.close()
 print "key校验完成，结果请查看checksum.out和log目录下check文件"