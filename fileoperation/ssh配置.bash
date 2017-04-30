#!/bin/sh
sudo apt-get install openssh-server		# 安装ssh
sudo ps -e | grep ssh		# 结果有sshd,说明ssh服务已经启动，如果没有启动，输入"sudo service ssh start启动服务。
sudo gedit /etc/ssh/sshd_config		# 修改配置文件中的"PermitRootLogin without-password"加一个"#"号,把它注释掉，再增加一句"PermitRootLogin yes"，保存，修改成功。port代表端口号，默认为22
ifconfig		# 查看IP

# 磁盘分区后要进行格式化分区，否则没有效果。
df -h		# 查看当前磁盘使用情况
df -l		# 查看新硬盘
fdisk /dev/sdb	# 硬盘分区，结合参数进行相关设置
mkfs -t ext3 /dev/sdb1	# 格式化分区
mkdir /data		# 创建挂载点
mount /dev/sdb1 /data	# 磁盘挂载
vi /etc/fstab		# 修改fstab文件
/dev/sdb1 /data ext3 defaults 1 2	# 添加该行实现开机自动挂载

