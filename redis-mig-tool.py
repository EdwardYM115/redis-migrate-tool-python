#!/usr/bin/python
#coding=utf-8
import os
print "**********************************************************"
print "*                                                        *"
print "*                                                        *"
print "*                                                        *"
print "*                                                        *"
print "*                京东云REDIS迁移工具                     *"
print "*                                                        *"
print "*                Version Python 1.0                      *"
print "*                                                        *"
print "*                 Powered By Edward                      *"
print "*                                                        *"
while 1:
 print "**********************************************************"
 print "*            输入'1':生成迁移配置文件                    *"
 print "*            输入'2':启动迁移进程                        *"
 print "*            输入'3':迁移日志概要                        *"
 print "*            输入'4':迁移数据校验                        *"
 print "*            输入'5':迁移数据key数量比对                 *"
 print "*            输入'6':停止迁移进程                        *"
 print "*            输入'7':删除迁移配置文件                    *"
 print "*            输入'8':退出                                *"
 print "**********************************************************"
 cmd=raw_input("请输入数字1~8执行操作：")
 if cmd == '1':
  os.system('python gen_cfg.py')
  os.system('sleep 2')
  os.system('python gen_mig.py')
  os.system('sleep 2')
  os.system('python gen_chk.py')
  print "全部配置文件生成完毕，建议再次确认hosts.txt、sourceDbSize.sh以及conf_mig目录和conf_chk目录下的conf文件是否正确配置"
 if cmd == '2':
  os.system('python start.py')
 if cmd == '3':
  os.system('python log_chk.py')
 if cmd == '4':
  os.system('python key_chk.py')
 if cmd == '5':
  os.system('python key_num')
 if cmd == '6':
  os.system('python stop.py')
 if cmd == '7':
  os.system('python cle_cfg.py')
 if cmd == '8':
  print "工具退出"
  break