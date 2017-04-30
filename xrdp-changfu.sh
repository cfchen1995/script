#!/bin/sh
# ssh登录进入ubuntu，查看此时vncserver所使用的端口
netstat -tunlp		# 查询相关连接端口
ps -ef | grep 1673	# 该命令可以查询相关进程及接口
sudo cat /vat/log/xrdp-sesman.log

