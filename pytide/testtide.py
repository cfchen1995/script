#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from earthtide import *

xsta = [4075578.385,931852.890,4801570.154];
xsun = [137859926952.015,54228127881.4350,23509422341.6960];
xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
yr = 2009;
month = 4;
day = 13;
fhr = 0;
dxtide = earthtide(xsta,yr,month,day,fhr,xsun,xmon);
tide = [0.7700420357108125891E-01,0.6304056321824967613E-01,0.5516568152597246810E-01];
error1 = [i-j for i, j in zip(dxtide, tide)]
print(error1)

xsta = [1112189.660,-4842955.026,3985352.284];
xsun = [-54537460436.2357,130244288385.279,56463429031.5996];
xmon = [300396716.912,243238281.451,120548075.939];
yr = 2012;
month = 7;
day = 13;
fhr = 0.00;
dxtide = earthtide(xsta,yr,month,day,fhr,xsun,xmon);
tide = [-0.2036831479592075833E-01,0.5658254776225972449E-01,-0.7597679676871742227E-01];
error2 = [i-j for i, j in zip(dxtide, tide)]
print(error2)

xsta = [1112200.5696,-4842957.8511,3985345.9122];
xsun = [100210282451.6279,103055630398.3160,56855096480.4475];
xmon = [369817604.4348,1897917.5258,120804980.8284];
yr = 2015;
month = 7;
day = 15;
fhr = 0.00;
dxtide = earthtide(xsta,yr,month,day,fhr,xsun,xmon);
tide = [0.00509570869172363845,0.0828663025983528700,-0.0636634925404189617];
error3 = [i-j for i, j in zip(dxtide, tide)]
print(error3)
