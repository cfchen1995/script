#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import *
def st1idiu(xsta, xsun, xmon, fac2sun, fac2mon):
    # 函数功能：
    #         计算由地幔滞弹性引起周日波的异相改正，单位为米，坐标
    # 输入参数：
    #         xsta、xsun和xmon分别代表IGS站、日月的地心坐标
    #         fac2sun,fac2mon分别代表日月的二阶引潮势(TGP)系数
    # 输出参数：
    #         xcorsta代表周日波的异相位移改正
    # 计算示例：
    #         xsta = [4075578.385,931852.890,4801570.154];
    #         xsun = [137859926952.015,54228127881.4350,23509422341.6960];
    #         xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
    #         fac2sun =  0.163271964478954;
    #         fac2mon =  0.321989090026845;
    # 结果：
    #         xcorsta = [-0.2836337012840008001D-03,0.1125342324347507444D-03,-0.2471186224343683169D-03];

    dhi = -0.0025
    dli = -0.0007
    # 计算IGS站、日月的位置距离
    # rmon = norm(xmon)
    # rsun = norm(xsun)
    # rsta = norm(xsta)    # 求取该点与原点的距离
    rmon = sqrt(xmon[0]**2 + xmon[1]**2 + xmon[2]**2)
    rsun = sqrt(xsun[0]**2 + xsun[1]**2 + xsun[2]**2)
    rsta = sqrt(xsta[0]**2 + xsta[1]**2 + xsta[2]**2)
    sinphi = xsta[2]/rsta
    # cosphi = norm(xsta(0:1))/rsta
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    cos2phi = cosphi*cosphi-sinphi*sinphi
    sinla = xsta[1]/cosphi/rsta
    cosla = xsta[0]/cosphi/rsta
    
    drsun = -3*dhi*sinphi*cosphi*fac2sun*xsun[2]*(xsun[0]*sinla-xsun[1]*cosla)/rsun**2
    drmon = -3*dhi*sinphi*cosphi*fac2mon*xmon[2]*(xmon[0]*sinla-xmon[1]*cosla)/rmon**2
    dnsun = -3*dli*cos2phi*fac2sun*xsun[2]*(xsun[0]*sinla-xsun[1]*cosla)/rsun**2
    dnmon = -3*dli*cos2phi*fac2mon*xmon[2]*(xmon[0]*sinla-xmon[1]*cosla)/rmon**2
    desun = -3*dli*sinphi*fac2sun*xsun[2]*(xsun[0]*cosla+xsun[1]*sinla)/rsun**2
    demon = -3*dli*sinphi*fac2mon*xmon[2]*(xmon[0]*cosla+xmon[1]*sinla)/rmon**2
    
    dr = drsun+drmon
    dn = dnsun+dnmon
    de = desun+demon
    
    # 数据应当先声明再使用
    xcorsta = [1]*3
    xcorsta[0] =dr*cosla*cosphi-de*sinla-dn*sinphi*cosla
    xcorsta[1] =dr*sinla*cosphi+de*cosla-dn*sinphi*sinla
    xcorsta[2] =dr*sinphi+dn*cosphi
    
    return xcorsta
