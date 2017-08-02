#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from dat import *
from st1idiu import *
from st1isem import *
from st1l1 import *
from step2diu import *
from step2lon import *

def dehanttideinel(xsta,yr,month,day,fhr,xsun,xmon):
    # 函数功能：
    #         计算由日月吸引引起测站位移改正
    #         分别调用函数：1）st1idiu + st1isem + st1l1
    #                       2）step2diu + step2lon
    # The IGS station is in ITRF co-rotating frame. All coordinates, X, Y, and Z, are expressed in meters.
    # The position is in Earth Centered Earth Fixed (ECEF) frame.  All coordinates are expressed in meters.
    # The time are expressed in Coordinated Universal Time (UTC).
    # 输入参数：
    #         xsta、xsun和xmon分别代表IGS站、日月的地心坐标
    #         date代表时间
    #         yr,month,day,fhr代表年月日及小数时
    # 输出参数：
    #         dxtide代表测站位移，坐标体系为地心ITRF坐标系统，the geocentric ITRF。
    # 
    # 计算示例一：
    #         xsta = [4075578.385,931852.890,4801570.154];
    #         xsun = [137859926952.015,54228127881.4350,23509422341.6960];
    #         xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
    #         date = [2009 4 13 0];
    #         yr = 2009;
    #         month = 4;
    #         day = 13;
    #         fhr = 0;
    #         dxtide = dehanttideinel(xsta,yr,month,day,fhr,xsun,xmon);
    # 结果：
    #         dxtide = [0.7700420357108125891E-01,0.6304056321824967613E-01,0.5516568152597246810E-01];
    # 计算示例二：
    #         xsta = [1112189.660,-4842955.026,3985352.284];
    #         xsun = [-54537460436.2357,130244288385.279,56463429031.5996];
    #         xmon = [300396716.912,243238281.451,120548075.939];
    #         yr = 2012;
    #         month = 7;
    #         day = 13;
    #         fhr = 0.00;
    #         dxtide = dehanttideinel(xsta,yr,month,day,fhr,xsun,xmon);
    # 结果：
    #         dxtide = [-0.2036831479592075833E-01,0.5658254776225972449E-01,-0.7597679676871742227E-01];
    # 计算示例三：
    #         xsta = [1112200.5696,-4842957.8511,3985345.9122];
    #         xsun = [100210282451.6279,103055630398.3160,56855096480.4475];
    #         xmon = [369817604.4348,1897917.5258,120804980.8284];
    #         yr = 2015;
    #         month = 7;
    #         day = 15;
    #         fhr = 0.00;
    #         dxtide = dehanttideinel(xsta,yr,month,day,fhr,xsun,xmon);
    # 结果：
    #         dxtide = [0.00509570869172363845,0.0828663025983528700,-0.0636634925404189617];
    
    # 若使用第二个函数运行则注释该行
    # [yr,month,day,fhr] = deal(date(1),date(2),date(3),date(4));
    # 二三阶勒夫数的标称值
    h20 = 0.6078
    l20 = 0.0847
    h3 = 0.292
    l3 = 0.015
    # 计算测站与日月的内积
    # rsta = norm(xsta);
    # rsun = norm(xsun);
    # rmon = norm(xmon);
    rmon = sqrt(xmon[0]**2 + xmon[1]**2 + xmon[2]**2)
    rsun = sqrt(xsun[0]**2 + xsun[1]**2 + xsun[2]**2)
    rsta = sqrt(xsta[0]**2 + xsta[1]**2 + xsta[2]**2)
    # scs = dot(xsta,xsun);
    # scm = dot(xsta,xmon);
    scs = sum(i*j for i, j in zip(xsta, xsun))
    scm = sum(i*j for i, j in zip(xsta, xmon))
    scsun = scs/rsta/rsun
    scmon = scm/rsta/rmon
    # 重新计算h2和l2
    # cosphi = norm(xsta(1:2))/rsta
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    h2 = h20-0.0006*(1-3/2*cosphi**2)
    l2 = l20+0.0002*(1-3/2*cosphi**2)
    # p2分量
    p2sun = 3*(h2/2-l2)*scsun**2-h2/2
    p2mon = 3*(h2/2-l2)*scmon**2-h2/2
    # p3分量
    p3sun = 5/2*(h3-3*l3)*scsun**3+3/2*(l3-h3)*scsun
    p3mon = 5/2*(h3-3*l3)*scmon**3+3/2*(l3-h3)*scmon
    
    # 日月方向的分量
    x2sun = 3*l2*scsun
    x2mon = 3*l2*scmon
    x3sun = 3*l3/2*(5*scsun**2-1)
    x3mon = 3*l3/2*(5*scmon**2-1)
    # IAU提供的日月参数
    mass_ratio_sun = 332946.0482
    mass_ratio_moon = 0.0123000371
    re = 6378136.6
    fac2sun = mass_ratio_sun*re*(re/rsun)**3
    fac2mon = mass_ratio_moon*re*(re/rmon)**3
    fac3sun = fac2sun*(re/rsun)
    fac3mon = fac2mon*(re/rmon)
    
    # 测站位移总和
    # dxtide = fac2sun.*( x2sun.*xsun./rsun + p2sun.*xsta./rsta ) +...
    #     fac2mon.*( x2mon.*xmon./rmon + p2mon.*xsta./rsta ) +...
    #     fac3sun.*( x3sun.*xsun./rsun + p3sun.*xsta./rsta ) +...
    #     fac3mon.*( x3mon.*xmon./rmon + p3mon.*xsta./rsta );
    dxtide = [0]*3
    for i in range(1,4):
        dxtide[i-1] = fac2sun*( x2sun*xsun[i-1]/rsun + p2sun*xsta[i-1]/rsta ) + \
                      fac2mon*( x2mon*xmon[i-1]/rmon + p2mon*xsta[i-1]/rsta ) + \
                      fac3sun*( x3sun*xsun[i-1]/rsun + p3sun*xsta[i-1]/rsta ) + \
                      fac3mon*( x3mon*xmon[i-1]/rmon + p3mon*xsta[i-1]/rsta )
    
    # 勒夫数的异相改正
    xcorsta = st1idiu(xsta,xsun,xmon,fac2sun,fac2mon)        # 周日波改正
    # dxtide = dxtide+xcorsta
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    xcorsta = st1isem(xsta,xsun,xmon,fac2sun,fac2mon)        # 半周日波改正
    # dxtide = dxtide+xcorsta
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    xcorsta = st1l1(xsta,xsun,xmon,fac2sun,fac2mon)          # 纬度依赖改正
    # dxtide = dxtide+xcorsta
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    # 第二步周日改正
    [jjm0,jjm1,j] = cal2jd(yr,month,day)        # 儒勒日计算
    fhrd = fhr/24
    t = ((jjm0-2451545.0)+jjm1+fhrd)/36525      # 儒勒日世纪数
    dtt = dat(yr,month,day,fhrd)                # 时间差计算
    dtt = dtt + 32.184
    t = t+dtt/(3600.0*24.0*36525)
    xcorsta = step2diu(xsta,fhr,t)              # 计算频率依赖的同异相改正
    # dxtide = dxtide+xcorsta
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    xcorsta = step2lon(xsta,t)                  # 长波长的同异相频率依赖改正
    # dxtide = dxtide+xcorsta
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    # # 第三步改正
    # # 对永久潮改正
    # sinphi = xsta(3)/rsta;
    # cosphi = norm(xsta(1:2))/rsta;
    # cosla = xsta(1)/cosphi/rsta;
    # sinla = xsta(2)/cosphi/rsta;
    # dr = -sqrt(5/4/pi)*h2*0.31460*(3/2*sinphi**2-0.5);
    # dn = -sqrt(5/4/pi)*l2*0.31460*3*cosphi*sinphi;
    # # 计算测站位移
    # dxtide(1)=dxtide(1)-dr*cosla*cosphi+dn*cosla*sinphi;
    # dxtide(2)=dxtide(2)-dr*sinla*cosphi+dn*sinla*sinphi;
    # dxtide(3)=dxtide(3)-dr*sinphi      -dn*cosphi;
    
    # error = [i-j for i, j in zip(dxtide, xtide)]
    return dxtide
    