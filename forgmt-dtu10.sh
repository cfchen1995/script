#!/bin/bash

declare -a lo
declare -a la
declare -a z
#####################################################################################################################################子函数开始
function m2gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下m2潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} m2.dtu10.tr.2010 gr.gbaver.wef.p02.ce g poly.tmp > /home/yxw/usr/DTU/m2.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/m2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/m2-gbaver.few
cat /home/yxw/usr/DTU/m2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/m2-gbaver.fns
cat /home/yxw/usr/DTU/m2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/m2-gbaver.fver
}
#####################################################子函数m2潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下m2潮波振幅相和相位

function n2gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下n2潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} n2.dtu10.tr.2010 gr.gbaver.wef.p02.ce g poly.tmp > /home/yxw/usr/DTU/n2.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/n2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/n2-gbaver.few
cat /home/yxw/usr/DTU/n2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/n2-gbaver.fns
cat /home/yxw/usr/DTU/n2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/n2-gbaver.fver
}
#####################################################子函数n2潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下n2潮波振幅相和相位

function s2gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下s2潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} s2.dtu10.tr.2010 gr.gbaver.wef.p02.ce gt poly.tmp > /home/yxw/usr/DTU/s2.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/s2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/s2-gbaver.few
cat /home/yxw/usr/DTU/s2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/s2-gbaver.fns
cat /home/yxw/usr/DTU/s2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/s2-gbaver.fver
}
#####################################################子函数s2潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下s2潮波振幅相和相位


function k2gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下k2潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} k2.dtu10.tr.2010 gr.gbaver.wef.p02.ce g poly.tmp > /home/yxw/usr/DTU/k2.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/k2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/k2-gbaver.few
cat /home/yxw/usr/DTU/k2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/k2-gbaver.fns
cat /home/yxw/usr/DTU/k2.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/k2-gbaver.fver
}
#####################################################子函数k2潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下k2潮波振幅相和相位


function k1gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下k1潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} k1.dtu10.tr.2010 gr.gbaver.wef.p02.ce g poly.tmp > /home/yxw/usr/DTU/k1.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/k1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/k1-gbaver.few
cat /home/yxw/usr/DTU/k1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/k1-gbaver.fns
cat /home/yxw/usr/DTU/k1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/k1-gbaver.fver
}
#####################################################子函数k1潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下k1潮波振幅相和相位

function p1gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下p1潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} p1.dtu10.tr.2010 gr.gbaver.wef.p02.ce g poly.tmp > /home/yxw/usr/DTU/p1.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/p1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/p1-gbaver.few
cat /home/yxw/usr/DTU/p1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/p1-gbaver.fns
cat /home/yxw/usr/DTU/p1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/p1-gbaver.fver
}
#####################################################子函数p1潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下p1潮波振幅相和相位


function o1gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下o1潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} o1.dtu10.tr.2010 gr.gbaver.wef.p02.ce g poly.tmp > /home/yxw/usr/DTU/o1.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/o1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/o1-gbaver.few
cat /home/yxw/usr/DTU/o1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/o1-gbaver.fns
cat /home/yxw/usr/DTU/o1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/o1-gbaver.fver
}
#####################################################子函数o1潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下o1潮波振幅相和相位


function q1gbaver {
################################################################################地球模型gbaver,计算全球海潮模型dtu10.tr.2010下q1潮波振幅相和相位

cd /home/yxw/spotl/working
../bin/polymake <<EOF> poly.tmp 
EOF
../bin/nloadf D$j ${la[$j]} ${lo[$j]} ${z[$j]} q1.dtu10.tr.2010 gr.gbaver.wef.p02.ce g poly.tmp > /home/yxw/usr/DTU/q1.dtu.gbaver.fg

##########################################################将负荷位移东西/南北/径向三个方向分别出入三个文件，每个文件中按照计算的点依次记录
#################################################################################抽取全球海潮模型dtu10.tr.2010计算结果中的径向和水平三个方向分量
cat /home/yxw/usr/DTU/q1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 90 >> /home/yxw/usr/DTU/q1-gbaver.few
cat /home/yxw/usr/DTU/q1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp d 0 >> /home/yxw/usr/DTU/q1-gbaver.fns
cat /home/yxw/usr/DTU/q1.dtu.gbaver.fg | /home/yxw/spotl/bin/harprp z >> /home/yxw/usr/DTU/q1-gbaver.fver
}
#####################################################子函数q1潮波########地球模型gbaver,计算全球海潮模型dtu10.tr.2010下q1潮波振幅相和相位

i=0
while read  t1 t2 t3 
do
lo[$i]=$t1
la[$i]=$t2
z[$i]=$t3
i=$[$i+1] 
done < data.ss
##########################################向循环中输入文件方式
l=${#la[@]}
let "l-=1"
cd /home/yxw/spotl/working
j=0
while [ $j -le $l ]
 do 
 m2gbaver $j
 n2gbaver $j
 s2gbaver $j
 k2gbaver $j
 k1gbaver $j
 p1gbaver $j
 o1gbaver $j
 q1gbaver $j
 j=$[$j+1] 
done
cd /home/yxw/usr/DTU
for m in m2 n2 s2 k2 k1 p1 o1 q1;do
 for n in few fns fver;do
   if [ $m = m2 -o $m = k2 -o $m = k1 ] 
   then
    awk '{if($7!=0.0000 && $7!="''")  print $0}' $m-gbaver.$n > $m-gbaverend.$n
   else
    awk '{if($6!=0.0000 && $6!="''")  print $0}' $m-gbaver.$n > $m-gbaverend.$n
   fi
 done
done
###############################################单潮波/单海潮模型/单地球模型/结果用于提供GMT输入文件程序m2-gbaverend.$n到m2-gbavergmt.$n

##提取站点经纬度
for m in m2 n2 s2 k2 k1 p1 o1 q1;do
 for n in few fns fver;do
   if [ $m = m2 -o $m = k2 -o $m = k1 ] 
   then
    awk '{print $7 " "$8}' $m-gbaverend.$n > $m-gbavergmt.$n
   else
    awk '{print $6 " "$7}' $m-gbaverend.$n > $m-gbavergmt.$n
   fi
 done
done
