#!/bin/sh
# 重力场数据下载
# 04/30/2017 西南交通大学
#
# 下载网页html文件，下载绝对路径
wget -k http://icgem.gfz-potsdam.de/ICGEM/shms/monthly/csr-rl05/

# 筛选出GSM（斜线 ’/’ 十分必要，因为DDK数据中也包含关键字GSM）
cat index.html | grep /GSM | cut -d '"' -f 6 > gsm.txt

# 如果需要DDK滤波的数据，筛选出DDK1
# cat index.html | grep DDK1  | cut -d '"' -f 6 > DDK1.txt

# 使用wget批量下载
wget -i gsm.txt

