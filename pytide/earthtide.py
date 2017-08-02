#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import *
from stepone import *
from steptwo import *

def earthtide(xsta,yr,month,day,fhr,xsun,xmon):
    # Function:
    #         the station corrections
    #         1) st1idiu + st1isem + st1l1
    #         2) step2diu + step2lon
    # The IGS station is in ITRF co-rotating frame. All coordinates, X, Y, and Z, are expressed in meters.
    # The position is in Earth Centered Earth Fixed (ECEF) frame.  All coordinates are expressed in meters.
    # The time are expressed in Coordinated Universal Time (UTC).
    # Input:
    #         xsta, xsun, xmon: Geocentric position of the IGS station, the Sun, the Moon
    #         iy, im, id, fd: UTC date of year, month, day, fraction of day
    # Output:
    #         dxtide: the station tidal displacement (the geocentric ITRF)
    # 
    # Example one:
    #         xsta = [4075578.385,931852.890,4801570.154];
    #         xsun = [137859926952.015,54228127881.4350,23509422341.6960];
    #         xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
    #         yr = 2009;
    #         month = 4;
    #         day = 13;
    #         fhr = 0;
    #         dxtide = dehanttideinel(xsta,yr,month,day,fhr,xsun,xmon);
    # Results:
    #         dxtide = [0.7700420357108125891E-01,0.6304056321824967613E-01,0.5516568152597246810E-01];
    # Example two:
    #         xsta = [1112189.660,-4842955.026,3985352.284];
    #         xsun = [-54537460436.2357,130244288385.279,56463429031.5996];
    #         xmon = [300396716.912,243238281.451,120548075.939];
    #         yr = 2012;
    #         month = 7;
    #         day = 13;
    #         fhr = 0.00;
    #         dxtide = dehanttideinel(xsta,yr,month,day,fhr,xsun,xmon);
    # Results:
    #         dxtide = [-0.2036831479592075833E-01,0.5658254776225972449E-01,-0.7597679676871742227E-01];
    # Example three:
    #         xsta = [1112200.5696,-4842957.8511,3985345.9122];
    #         xsun = [100210282451.6279,103055630398.3160,56855096480.4475];
    #         xmon = [369817604.4348,1897917.5258,120804980.8284];
    #         yr = 2015;
    #         month = 7;
    #         day = 15;
    #         fhr = 0.00;
    #         dxtide = dehanttideinel(xsta,yr,month,day,fhr,xsun,xmon);
    # Results:
    #         dxtide = [0.00509570869172363845,0.0828663025983528700,-0.0636634925404189617];
    
    # 二三阶勒夫数的标称值
    h20 = 0.6078
    l20 = 0.0847
    h3 = 0.292
    l3 = 0.015
    
    # compute the dot product
    rmon = sqrt(xmon[0]**2 + xmon[1]**2 + xmon[2]**2)
    rsun = sqrt(xsun[0]**2 + xsun[1]**2 + xsun[2]**2)
    rsta = sqrt(xsta[0]**2 + xsta[1]**2 + xsta[2]**2)
    
    scs = sum(i*j for i, j in zip(xsta, xsun))
    scm = sum(i*j for i, j in zip(xsta, xmon))
    scsun = scs/rsta/rsun
    scmon = scm/rsta/rmon
    
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    h2 = h20-0.0006*(1-3/2*cosphi**2)
    l2 = l20+0.0002*(1-3/2*cosphi**2)
    
    # p2
    p2sun = 3*(h2/2-l2)*scsun**2-h2/2
    p2mon = 3*(h2/2-l2)*scmon**2-h2/2
    
    # p3
    p3sun = 5/2*(h3-3*l3)*scsun**3+3/2*(l3-h3)*scsun
    p3mon = 5/2*(h3-3*l3)*scmon**3+3/2*(l3-h3)*scmon
    
    # the Sun and the Moon
    x2sun = 3*l2*scsun
    x2mon = 3*l2*scmon
    x3sun = 3*l3/2*(5*scsun**2-1)
    x3mon = 3*l3/2*(5*scmon**2-1)
    # IAU
    mass_ratio_sun = 332946.0482
    mass_ratio_moon = 0.0123000371
    re = 6378136.6
    fac2sun = mass_ratio_sun*re*(re/rsun)**3
    fac2mon = mass_ratio_moon*re*(re/rmon)**3
    fac3sun = fac2sun*(re/rsun)
    fac3mon = fac2mon*(re/rmon)
    
    dxtide = [0]*3
    for i in range(1,4):
        dxtide[i-1] = fac2sun*( x2sun*xsun[i-1]/rsun + p2sun*xsta[i-1]/rsta ) + \
                      fac2mon*( x2mon*xmon[i-1]/rmon + p2mon*xsta[i-1]/rsta ) + \
                      fac3sun*( x3sun*xsun[i-1]/rsun + p3sun*xsta[i-1]/rsta ) + \
                      fac3mon*( x3mon*xmon[i-1]/rmon + p3mon*xsta[i-1]/rsta )
    
    
    xcorsta = st1idiu(xsta,xsun,xmon,fac2sun,fac2mon)        # diurnal band
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    xcorsta = st1isem(xsta,xsun,xmon,fac2sun,fac2mon)        # semi-diurnal band
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    xcorsta = st1l1(xsta,xsun,xmon,fac2sun,fac2mon)          # latitude dependence
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    # the second step
    [jjm0,jjm1,j] = cal2jd(yr,month,day)        # MJD
    fhrd = fhr/24
    t = ((jjm0-2451545.0)+jjm1+fhrd)/36525      # MJD century
    dtt = dat(yr,month,day,fhrd)                # TAI-UTC
    dtt = dtt + 32.184
    t = t+dtt/(3600.0*24.0*36525)
    xcorsta = step2diu(xsta,fhr,t)              # frequency dedenpence of diurnal band
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    xcorsta = step2lon(xsta,t)                  # frequency dependence of long-period band
    dxtide = [i+j for i, j in zip(dxtide, xcorsta)]
    
    # # the third step
    # # the permanent tidal corrections
    # sinphi = xsta(3)/rsta;
    # cosphi = norm(xsta(1:2))/rsta;
    # cosla = xsta(1)/cosphi/rsta;
    # sinla = xsta(2)/cosphi/rsta;
    # dr = -sqrt(5/4/pi)*h2*0.31460*(3/2*sinphi**2-0.5);
    # dn = -sqrt(5/4/pi)*l2*0.31460*3*cosphi*sinphi;
    # # the tidal displacement
    # dxtide(1)=dxtide(1)-dr*cosla*cosphi+dn*cosla*sinphi;
    # dxtide(2)=dxtide(2)-dr*sinla*cosphi+dn*sinla*sinphi;
    # dxtide(3)=dxtide(3)-dr*sinphi      -dn*cosphi;
    
    # error = [i-j for i, j in zip(dxtide, xtide)]
    return dxtide
    