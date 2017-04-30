#!/bin/bash
# 参考：http://wiki.ubuntu.org.cn/ADSL%EF%BC%88PPPOE%EF%BC%89%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97
# 	http://www.cnblogs.com/jhldreams/p/4161123.html

# 以下的操作只能处理位于同一局域网的电脑的连接。
# 这个问题还有待于进行进一步的处理研究，学习如何使用ssh和nat123的相关技术实现问题的处理。

sudo ifconfig eth0 up
sudo pppoeconf
# 需要的时候启动ADSL连接，可以在终端中输入
sudo pon dsl-provider
# 断开ADSL连接，可以在终端中输入
sudo poff
# 查看日志，可以在终端中输入
plog
# 获得接口信息，可以在终端中输入
ifconfig ppp0

# 使用pppoeconf拨号后，Network Manager显示设备未托管的解决办法
# 在终端中输入以下命令，来配置网络连接管理文件
sudo gedit /etc/NetworkManager/nm-system-settings.conf
# 打开后，找到 [ifupdown] managed=false 修改成： [ifupdown] managed=true
sudo gedit /etc/network/interfaces
auto lo iface lo inet loopback		# 保留
# 删除dns设置
sudo mv /etc/resolv.conf /etc/resolv.conf_backup
# 之后重启 network-manager服务
sudo service network-manager restart 
