#!/bin/sh
# 利用GAMIT进行大气可降水量的解算
# sh_gamit -expt demo -d 2016 255 -met -metutil Z	# Z-文件文件获取可降水量
# sh_metutil -f <o-file> -m <met-file>				# O-文件文件获取可降水量
#
# 陈昌福 04/29/2017

# 下载获取相应站点的IGS数据。

# 公用表链接
sh_setup -yr 2016 -doy 255
# 检查其中的 map.grid 是否正确链接至对应的VMF1 映射函数模型。
ls -l tables/map.grid
rm -f tables/map.grid     # 删除原始链接
ln -s ~/gg/tables/vmf1grd.2016* tables/map.grid   # 创建新链接。如果你处理的不是 2016 年的观测数据，使用实际的年替换这里的 “2016”

# 参数配置
# 打开 sestbl.，将其中对应的项修改为
# Met obs source = RNX UFL GPT 50 　 ; hierarchical list with humidity value at the end; e.g. RNX UFL GPT 50 ; default GTP 50
# Output met = Y 　　 ; write the a priori met values to a z-file (Y/N)
# 其中 “Met obs source = RNX UFL GPT 50” 表示需要测站处的温度和气压等气象观测数据时，首先检查工程目录的 met 文件夹中有没有对应测站的 RINEX 气象文件，然后检查有无 U-文件中有无该站的信息，最后才采用 GPT 模型中的值。末尾的 “50” 表示假设的相对湿度，默认为 50%。也可以对其进行更改，但实际上该值对解算结果影响很小。
# “Output met = Y” 一项，表示设置 GAMIT 程序在基线解算的同时输出对气象参数的估计值，这些结果将保存至 Z-文件中。
# 同样在 sestbl. 文件中，将映射函数修改为使用 VMF1：
# DMap = VMF1 　　 ; GMF(default)/VMF1/NMFH; GMF now invokes GPT2 if gpt.grid is available (default)
# WMap = VMF1 　　 ; GMF(default)/VMF1/NMFW; GMF now invokes GPT2 if gpt.grid is available (default)
# Use map.list = N 　 ; VMF1 list file with mapping functions, ZHD, ZWD, P, Pw, T, Ht
# Use map.grid = Y 　 ; VMF1 grid file with mapping functions and ZHD

# 基线解算
sh_gamit -expt demo -d 2016 255 -met		# -met 参数指示在解算时引入 RINEX 格式的气象观测数据。
# 上述解算结果的Z-文件，其中并没有 PWV 解算结果而只有对流层总延迟和干延迟等参数信息，还需要执行 sh_metutil 命令做进一步处理。
# 该语句的语法为sh_metutil -f <o-file> -z <z-file> 其中 <o-file> 代表基线解算结果的 O-文件，<z-file> 代表输出的 Z-文件。
sh_metutil -f odemoa.255 -z z*.255			# 其可降水汽解算成果保存在以 “met” 开头的文件中。

# 补充说明
# 可在基线解算完成后直接生成可降水汽的估计值，可以为 sh_gamit 命令多加一个 -metutil Z 参数。如：
sh_gamit -expt demo -d 2016 255 -met -metutil Z
# 另外，除了使用 Z-文件估计可降水汽，sh_metutil 命令还支持由测站的气象观测数据和基线解算得到的 O-文件生成可降水汽估计值。其命令为：
sh_metutil -f <o-file> -m <met-file>
# 在该命令中，<o-file> 代表基线解算结果的 O-文件，<met-file> 代表站点气象观测数据。
