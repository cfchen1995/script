#!/bin/sh
sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/		# 将下载源加入到系统的源列表
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -		# 导入谷歌软件的公钥
sudo apt-get update
sudo apt-get install google-chrome-stable	# 稳定版

