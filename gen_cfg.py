#!/usr/bin/python
#coding=utf-8
import linecache
f1=open("info.txt","r")
f2=open("hosts.txt","w")
count = len(f1.readlines())
i=8
j=1 
while i < count+1:
   SOURCEURL=linecache.getline("info.txt",i)
   f2.write(SOURCEURL.rstrip()+"\n")
   i+=1

JDCAUTH=linecache.getline("info.txt",2)
SOURCEAUTH=linecache.getline("info.txt",4)
JDCURL=linecache.getline("info.txt",6)
f1.close()
f2.close()

f3=open("rmt.conf","r")
content=f3.readlines()
f3.close()
f3=open("rmt.conf","w+")
if(SOURCEAUTH.strip() == ""):
  for line in content:
   if(j == 3):
     j+=1
     continue
   else:
     a=line.replace("JDCAUTH",JDCAUTH.rstrip()).replace("JDCURL",JDCURL.rstrip())
     f3.writelines(a)
     j+=1
else:
  for line in content:
    a=line.replace("SOURCEAUTH",SOURCEAUTH.rstrip()).replace("JDCAUTH",JDCAUTH.rstrip()).replace("JDCURL",JDCURL.rstrip())
    f3.writelines(a)
f3.close()

f4=open("sourceDbSize.py","r")
content=f4.readlines()
f4.close()
f4=open("sourceDbSize.py","w+")
for line in content:
 a=line.replace("PASSWORD",SOURCEAUTH.rstrip())
 f4.writelines(a)
f4.close()

print "基础配置文件生成完毕！"