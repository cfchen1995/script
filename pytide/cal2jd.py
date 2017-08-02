#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def cal2jd(iy,im,id):
    # 函数功能：
    #       通用时间转化为简化儒勒日
    # 输入参数：
    #       iy,im,id代表通用年月日
    # 输出参数：
    #       djm0代表J2000的儒勒日时间，djm为简化儒勒日时间
    #       j为标记参数
    # 计算示例：
    #       iy=2016;im=5;id=28;
    #       [djm0,djm,j] = cal2jd(iy,im,id);
    # 结果：
    #       djm=57536;
    iymin = -4799
    mtab = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    j = 0
    if ( iy < iymin ):
        j = -1
    else:
        if (im < 1 or im > 12):
            j=-2
        else:
            ly = ((im == 2) and (not (iy%4)) and ((iy%100) or not (iy%400)))
            if ( (id < 1) or (id > (mtab[im-1] + ly))):
                j = -3
            else:
                my = int((im-14)/12)
                iypmy = iy + my
                djm0 = 2400000.5
                djm = int((1461*(iypmy+4800))/4) \
                    + int((367*(im-2-12*my))/12) \
                    - int((3*((iypmy+4900)/100))/4) \
                    + id - 2432076
            
        
    
    return djm0,djm,j
