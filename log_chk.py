#!/usr/bin/python
#coding=utf-8
import os
path="log"
list1=['Not Finished:']
list2=['I/O error:']
list3=['Lost connect:']
files = os.listdir(path)
count_fin=0
count_io=0
count_con=0
i=0
j=15000
filenum=0
f=open('hosts.txt','r')
hostnum=len(f.readlines())
f.close()
for file in files:
 if os.path.splitext(file)[1] == ".log":
  filenum+=1
while i < filenum:
 sig_fin=0
 sig_io=0
 sig_con=0
 f=open('log/'+str(j)+'.log',"r")
 content=f.readlines()
 target1="All nodes' rdb file parsed finished for this write thread(0)"
 target2="I/O error"
 target3="lost connect"
 for line in content:
  if (target1 in line):
   sig_fin=1
  if (target2 in line):
   sig_io=1
  if (target3 in line):  
   sig_con=1
 if (sig_fin == 0):
  list1.append(str(j)+'.log')
 else:
  count_fin+=1
 if (sig_io == 1):
  list2.append(str(j)+'.log')
  count_io+=1
 if (sig_con == 1):
  list3.append(str(j)+'.log')
  count_con+=1
 i+=1
 j+=1
 f.close()
print "迁移日志概要，完整日志请查看log目录下log文件："
if (count_fin == hostnum):
 print "All parsed finished!"
else:
 print "Parsed finished:",count_fin
 print list1
if (count_io == 0):
 print "No I/O error"
else:
 print "I/O error:",count_io
 print list2
if (count_con == 0):
 print "No Lost connect"
else:
 print "Lost connect:",count_con
 print list3