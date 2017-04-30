#!/bin/bash
# Widows 7 访问Ubuntu 16.04 桌面系统
# Win7远程连接上Ubuntu，所使用的协议是rdp
sudo apt-get install xrdp
sudo apt-get install vnc4server tightvncserver		# 要安装tightvncserver，否则无法打开桌面
# 安装完成后，在“首选项—远程桌面”那里，设置好，允许远程桌面，允许控制。
# 在Win7打开mstsc，输入IP，用户名和密码。选择sessman-xvnc登录
# 例外：
# xrdp支持不了13.10的gnome了，解决办法是装个xfce界面， 
sudo apt-get install xubuntu-desktop
# 确定相应的登录桌面	该命令的作用是由于安装了 gnome桌面，ubuntu12.04中同时存在unity、GNOME多个桌面管理器，需要启动的时候指定一个，不然即使远程登录验证成功以后，也只是背景。
echo xfce4-session > ~/.xsession 
# 再设置配置文件
sudo gedit /etc/xrdp/startwm.sh
# 在. /etc/X11/Xsession 前一行插入
xfce4-session
# 重启xrdp
sudo service xrdp restart
