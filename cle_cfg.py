#!/usr/bin/python
#coding=utf-8
import os
import commands
procnum=commands.getstatusoutput('ps -ef|grep redis-migrate-tool|wc -l')
if ( procnum[1] == '2' ):
 os.system('rm -f conf_mig/*.conf')
 os.system('rm -f conf_chk/*.conf')
 print "已清空目录conf_mig和conf_chk下的配置文件"
else:
 print "尚有迁移进程未结束，不能清空配置"