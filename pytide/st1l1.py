#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import *
def st1l1(xsta,xsun,xmon,fac2sun,fac2mon):
    # 函数功能：
    #     计算由纬度依赖引起的改正
    # 输入参数：
    #     xsta、xsun和xmon分别代表IGS站、日月的地心坐标
    #     fac2sun,fac2mon分别代表日月的二阶引潮势(TGP)系数
    # 输出参数：
    #     xcorsta代表半周日波的异相位移改正
    # 计算示例：
    #      xsta = [4075578.385,931852.890,4801570.154];
    #      xsun = [137859926952.015,54228127881.4350,23509422341.6960];
    #      xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
    #      fac2sun =  0.163271964478954;
    #      fac2mon =  0.321989090026845;
    # 结果：
    #      xcorsta = [0.2367189532359759044D-03,0.5181609907284959182D-03,-0.3014881422940427977D-03];
    
    l1d = 0.0012
    l1sd = 0.0024
    # 计算IGS站及日月的位置距离
    # rmon = norm(xmon);
    # rsun = norm(xsun);
    # rsta = norm(xsta);
    rmon = sqrt(xmon[0]**2 + xmon[1]**2 + xmon[2]**2)
    rsun = sqrt(xsun[0]**2 + xsun[1]**2 + xsun[2]**2)
    rsta = sqrt(xsta[0]**2 + xsta[1]**2 + xsta[2]**2)
    sinphi = xsta[2]/rsta
    # cosphi = norm(xsta(1:2))/rsta;
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    sinla = xsta[1]/cosphi/rsta
    cosla = xsta[0]/cosphi/rsta
    # 计算周日波的位移改正
    l1 = l1d
    dnsun = -l1*sinphi**2*fac2sun*xsun[2]*(xsun[0]*cosla+xsun[1]*sinla)/rsun**2
    dnmon = -l1*sinphi**2*fac2mon*xmon[2]*(xmon[0]*cosla+xmon[1]*sinla)/rmon**2
    desun = l1*sinphi*(cosphi**2-sinphi**2)*fac2sun*xsun[2]*(xsun[0]*sinla-xsun[1]*cosla)/rsun**2
    demon = l1*sinphi*(cosphi**2-sinphi**2)*fac2mon*xmon[2]*(xmon[0]*sinla-xmon[1]*cosla)/rmon**2
    
    de = 3*(desun+demon)
    dn = 3*(dnsun+dnmon)
    
    xcorsta = [1]*3
    xcorsta[0] = 0
    xcorsta[1] = de
    xcorsta[2] = dn
    xcorsta[0] = -de*sinla-dn*sinphi*cosla
    xcorsta[1] = de*cosla-dn*sinphi*sinla
    xcorsta[2] = dn*cosphi
    # 计算半周日波的位移改正
    l1 = l1sd
    costwola = cosla**2-sinla**2
    sintwola = 2.0*cosla*sinla
    
    dnsun = -l1/2*sinphi*cosphi*fac2sun*((xsun[0]**2-xsun[1]**2)*costwola+2*xsun[0]*xsun[1]*sintwola)/rsun**2
    dnmon = -l1/2*sinphi*cosphi*fac2mon*((xmon[0]**2-xmon[1]**2)*costwola+2*xmon[0]*xmon[1]*sintwola)/rmon**2
    desun = -l1/2*sinphi**2*cosphi*fac2sun*((xsun[0]**2-xsun[1]**2)*sintwola-2*xsun[0]*xsun[1]*costwola)/rsun**2
    demon = -l1/2*sinphi**2*cosphi*fac2mon*((xmon[0]**2-xmon[1]**2)*sintwola-2*xmon[0]*xmon[1]*costwola)/rmon**2
    
    de = 3*(desun+demon)
    dn = 3*(dnsun+dnmon)
    
    # 计算测站位移
    xcorsta[0] = xcorsta[0]-de*sinla-dn*sinphi*cosla
    xcorsta[1] = xcorsta[1]+de*cosla-dn*sinphi*sinla
    xcorsta[2] = xcorsta[2]+dn*cosphi
    
    return xcorsta
