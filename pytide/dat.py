#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cal2jd import cal2jd

def dat(iy,im,id,fd):
    # 函数功能：
    #       计算给定时间的TAI和UTC的差值
    #       最近的闰秒：2015年06月30日
    # 输入参数：
    #       iy,im,id,fd代表UTC时间的年月日及小数日
    # 输出参数：
    #       deltat代表TAI与UTC的时间差，单位为seconds
    #       j为标记参数
    
    # Release year for this version of iauDat
    IYV = 2015
    
    # Reference dates (MJD) and drift rates (s/day), pre leap seconds
    drift = [[37300.0, 0.0012960],
             [37300.0, 0.0012960],
             [37300.0, 0.0012960],
             [37665.0, 0.0011232],
             [37665.0, 0.0011232],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [38761.0, 0.0012960],
             [39126.0, 0.0025920],
             [39126.0, 0.0025920]]
    
    # Number of Delta(AT) expressions before leap seconds were introduced 
    # [NERA1, ~] = size(drift)
    NERA1 = len(drift)
    
    # iyear month  Delta(AT)
    changes = [[1960,  1,  1.4178180],
               [1961,  1,  1.4228180],
               [1961,  8,  1.3728180],
               [1962,  1,  1.8458580],
               [1963, 11,  1.9458580],
               [1964,  1,  3.2401300],
               [1964,  4,  3.3401300],
               [1964,  9,  3.4401300],
               [1965,  1,  3.5401300],
               [1965,  3,  3.6401300],
               [1965,  7,  3.7401300],
               [1965,  9,  3.8401300],
               [1966,  1,  4.3131700],
               [1968,  2,  4.2131700],
               [1972,  1, 10.0      ],
               [1972,  7, 11.0      ],
               [1973,  1, 12.0      ],
               [1974,  1, 13.0      ],
               [1975,  1, 14.0      ],
               [1976,  1, 15.0      ],
               [1977,  1, 16.0      ],
               [1978,  1, 17.0      ],
               [1979,  1, 18.0      ],
               [1980,  1, 19.0      ],
               [1981,  7, 20.0      ],
               [1982,  7, 21.0      ],
               [1983,  7, 22.0      ],
               [1985,  7, 23.0      ],
               [1988,  1, 24.0      ],
               [1990,  1, 25.0      ],
               [1991,  1, 26.0      ],
               [1992,  7, 27.0      ],
               [1993,  7, 28.0      ],
               [1994,  7, 29.0      ],
               [1996,  1, 30.0      ],
               [1997,  7, 31.0      ],
               [1999,  1, 32.0      ],
               [2006,  1, 33.0      ],
               [2009,  1, 34.0      ],
               [2012,  7, 35.0      ],
               [2015,  7, 36.0      ]]
    
    # Number of Delta(AT) changes 
    # [NDAT, ~] = size(changes)
    NDAT = len(changes)
    
    # If invalid fraction of a day, set error status and give up. 
    if (fd < 0 or fd > 1):
        print('invalid fraction of a day')
    
    
    # Convert the date into an MJD. 
    [djm0, djm, j] = cal2jd(iy, im, id)
    
    # If pre-UTC year, set warning status and give up. 
    if (iy < changes[0][0]):
        print('pre-UTC year')
    
    
    # If suspiciously late year, set warning status but proceed. 
    if (iy > IYV + 5):
        print('suspiciously late year')
    
    
    # Combine year and month to form a date-ordered integer... 
    m = 12*iy + im
    
    # ...and use it to find the preceding table entry.
    for i in range(NDAT,1,-1):
        if (m >= (12 * changes[i-1][0] + changes[i-1][1])): 
            break
        
    
    
    # Get the Delta(AT)
    da = changes[i-1][2]
    
    # If pre-1972, adjust for drift
    if ((i-1) < NERA1):
        da = da + (djm + fd - drift[i-1][0]) * drift[i-1][1]
    
    
    # Return the Delta(AT) value
    deltat = da
    return deltat
    
    
####+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++####
#    # 另一种版本##########################################################
#    # 数据初始化
#    iyv = 2015                 # 最近的闰秒
#    ndat = 41                  # 闰秒总数
#    nera1 = 14                 # 引进闰秒时的时间差个数
#    da = 0                     # 结果的中间量的初始化
#    # idat = zeros(2,ndat);     # 时间改变时的起始年月
#    # dats = zeros(1,ndat);     # 给定时间的时间差
#    # drift = zeros(2,nera1);   # 参考时间点（MJD）及时间改变率
#    # js = 0;                   # 标记初始化，确保时间有效
#    
#    # [idat,dats,drift] = number;
#    idat = [[1960,1961,1961,1962,1963,1964,1964,1964,1965,1965,1965,1965,\
#             1966,1968,1972,1972,1973,1974,1975,1976,1977,1978,1979,1980,\
#             1981,1982,1983,1985,1988,1990,1991,1992,1993,1994,1996,1997,1999,2006,2009,2012,2015],\
#            [1,1,8,1,11,1,4,9,1,3,7,9,1,2,1,7,1,1,1,1,1,1,1,1,7,7,7,7,1,1,1,7,7,7,1,7,1,1,1,7,7]]
#    dats = [1.417818,1.422818,1.372818,1.845858,1.945858,3.24013,3.34013,\
#            3.44013,3.54013,3.64013,3.74013,3.84013,4.31317,4.21317,10,11,\
#            12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
#    drift = [[37300,37300,37300,37665,37665,38761,38761,38761,38761,38761,\
#             38761,38761,39126,39126],\
#            [0.001296,0.001296,0.001296,0.0011232,0.0011232,0.001296,0.001296,
#             0.001296,0.001296,0.001296,0.001296,0.001296,0.002592,0.002592]]
#    
#    # 小数日不在范围内
#    if ( fd<0 or fd>1 ):
#        js = -4
#        deltat = da
#        j = js
#        print('小数日应位于0和1之间！！')
#    else:
#        [djm0,djm,js] = cal2jd(iy,im,id)    # 日期转化为MJD
#        # 日期有问题
#        if ( js < 0 ):
#            deltat = da
#            j = js
#            print('日期无效！！')
#        
#        # 超出可计算的有闰秒的年份
#        if ( iy < idat[0][0] ):
#            js = 1
#            deltat = da
#            j = js
#            print('年份应小于1960！')
#        
#        # 与最近闰秒相差太大，提出警告，但接着计算
#        if ( iy > iyv+5 ):
#            js = 1
#        
#        m = 12*iy+im     # 综合年月
#        # 查找最接近的时间点
#        bis = 0
#        more = 1
#        for n in range(ndat,1,-1):    # 默认步长为1，否则要注明
#            if (more==1):
#                bis = n
#                more = m < (12*idat[0][n-1]+idat[1][n-1])
#        
#        # 计算警告
#        if ( bis < 1 ):
#            js = -5
#            deltat = da
#            j = js
#            print('计算有误！')
#        
#        da = dats[bis-1]    # 获取时间差
#        if ( bis <= nera1 ): # 1972年前的时间差
#            da = da + ( djm + fd - drift[0][bis-1]) * drift[1][bis-1]
#        
#        deltat = da
#        j = js
#    
#    return deltat,j
#
####+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++####
