#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Changfu Chen, Southwest Jiaotong University
# August 01, 2017
# 

from math import *
from datetime import *

# ====================================================================
# stepone package
# --------------------------------------------------------------------
# Subroutine: Gives the out-of-phase corrections induced by mantle 
#     anelasticity in the semi-diurnal band.
# --------------------------------------------------------------------
def st1isem(xsta,xsun,xmon,fac2sun,fac2mon):
    # Function:
    #       Gives the out-of-phase corrections induced by mantle 
    #       anelasticity in the semi-diurnal band.
    # Input:
    #       xsta, xsun, xmon: Geocentric position of the IGS station, the Sun, the Moon
    #       fac2sun, fac2mon: Degree two TGP factor for the Sun, the Moon
    # Output:
    #       xcorsta: Out-of-phase corrections for the semi-diurnal band
    # Example:
    #       xsta = [4075578.385,931852.890,4801570.154];
    #       xsun = [137859926952.015,54228127881.4350,23509422341.6960];
    #       xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
    #       fac2sun =  0.163271964478954;
    #       fac2mon =  0.321989090026845;
    # Results:
    #       xcorsta = [-0.2801334805106874015E-03,0.2939522229284325029E-04,-0.6051677912316721561E-04];
    
    dhi = -0.0022
    dli = -0.0007
    
    # the normalized position vector
    rmon = sqrt(xmon[0]**2 + xmon[1]**2 + xmon[2]**2)
    rsun = sqrt(xsun[0]**2 + xsun[1]**2 + xsun[2]**2)
    rsta = sqrt(xsta[0]**2 + xsta[1]**2 + xsta[2]**2)
    sinphi = xsta[2]/rsta
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    sinla = xsta[1]/cosphi/rsta
    cosla = xsta[0]/cosphi/rsta
    costwola = cosla*cosla-sinla*sinla
    sintwola = 2*cosla*sinla
    
    drsun = -3/4*dhi*cosphi**2*fac2sun*((xsun[0]**2-xsun[1]**2)*sintwola-2*xsun[0]*xsun[1]*costwola)/rsun**2
    drmon = -3/4*dhi*cosphi**2*fac2mon*((xmon[0]**2-xmon[1]**2)*sintwola-2*xmon[0]*xmon[1]*costwola)/rmon**2
    dnsun = 3/2*dli*sinphi*cosphi*fac2sun*((xsun[0]**2-xsun[1]**2)*sintwola-2*xsun[0]*xsun[1]*costwola)/rsun**2
    dnmon = 3/2*dli*sinphi*cosphi*fac2mon*((xmon[0]**2-xmon[1]**2)*sintwola-2*xmon[0]*xmon[1]*costwola)/rmon**2
    desun = -3/2*dli*cosphi*fac2sun*((xsun[0]**2-xsun[1]**2)*costwola+2*xsun[0]*xsun[1]*sintwola)/rsun**2
    demon = -3/2*dli*cosphi*fac2mon*((xmon[0]**2-xmon[1]**2)*costwola+2*xmon[0]*xmon[1]*sintwola)/rmon**2
    
    dr = drsun+drmon
    dn = dnsun+dnmon
    de = desun+demon
    
    # compute the semi-diurnal corrections
    xcorsta = [0]*3
    xcorsta[0] = dr*cosla*cosphi-de*sinla-dn*sinphi*cosla
    xcorsta[1] = dr*sinla*cosphi+de*cosla-dn*sinphi*sinla
    xcorsta[2] = dr*sinphi+dn*cosphi
    
    return xcorsta
    
# --------------------------------------------------------------------
# Subroutine: Gives the out-of-phase corrections induced by mantle 
#     anelasticity in the diurnal band.
# --------------------------------------------------------------------
def st1idiu(xsta, xsun, xmon, fac2sun, fac2mon):
    # Function:
    #       Gives the out-of-phase corrections induced by mantle 
    #       anelasticity in the diurnal band.
    # Input:
    #       xsta, xsun, xmon: Geocentric position of the IGS station, the Sun, the Moon
    #       fac2sun, fac2mon: Degree two TGP factor for the Sun, the Moon
    # Output:
    #       xcorsta: Out-of-phase corrections for the diurnal band
    # Example:
    #         xsta = [4075578.385,931852.890,4801570.154];
    #         xsun = [137859926952.015,54228127881.4350,23509422341.6960];
    #         xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
    #         fac2sun =  0.163271964478954;
    #         fac2mon =  0.321989090026845;
    # Results:
    #         xcorsta = [-0.2836337012840008001E-03,0.1125342324347507444E-03,-0.2471186224343683169E-03];

    dhi = -0.0025
    dli = -0.0007
    
    # the normalized position vector
    rmon = sqrt(xmon[0]**2 + xmon[1]**2 + xmon[2]**2)
    rsun = sqrt(xsun[0]**2 + xsun[1]**2 + xsun[2]**2)
    rsta = sqrt(xsta[0]**2 + xsta[1]**2 + xsta[2]**2)
    sinphi = xsta[2]/rsta
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
    
    # compute the diurnal corrections
    xcorsta = [0]*3
    xcorsta[0] =dr*cosla*cosphi-de*sinla-dn*sinphi*cosla
    xcorsta[1] =dr*sinla*cosphi+de*cosla-dn*sinphi*sinla
    xcorsta[2] =dr*sinphi+dn*cosphi
    
    return xcorsta
    
# --------------------------------------------------------------------
# Subroutine: Gives the corrections induced by latitude dependence 
#     given by L^1 in Mathews.
# --------------------------------------------------------------------
def st1l1(xsta,xsun,xmon,fac2sun,fac2mon):
    # Function:
    #     Gives the corrections induced by latitude dependence given by L^1.
    # Input:
    #       xsta, xsun, xmon: Geocentric position of the IGS station, the Sun, the Moon
    #       fac2sun, fac2mon: Degree two TGP factor for the Sun, the Moon
    # Output:
    #       xcorsta: Out-of-phase corrections for the semi-diurnal band
    # Example:
    #      xsta = [4075578.385,931852.890,4801570.154];
    #      xsun = [137859926952.015,54228127881.4350,23509422341.6960];
    #      xmon = [-179996231.920342,-312468450.131567,-169288918.592160];
    #      fac2sun =  0.163271964478954;
    #      fac2mon =  0.321989090026845;
    # Results:
    #      xcorsta = [0.2367189532359759044E-03,0.5181609907284959182E-03,-0.3014881422940427977E-03];
    
    l1d = 0.0012
    l1sd = 0.0024
    
    # the normalized position vector
    rmon = sqrt(xmon[0]**2 + xmon[1]**2 + xmon[2]**2)
    rsun = sqrt(xsun[0]**2 + xsun[1]**2 + xsun[2]**2)
    rsta = sqrt(xsta[0]**2 + xsta[1]**2 + xsta[2]**2)
    sinphi = xsta[2]/rsta
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    sinla = xsta[1]/cosphi/rsta
    cosla = xsta[0]/cosphi/rsta
    
    # compute the station corrections for the semi-diurnal band.
    l1 = l1d
    dnsun = -l1*sinphi**2*fac2sun*xsun[2]*(xsun[0]*cosla+xsun[1]*sinla)/rsun**2
    dnmon = -l1*sinphi**2*fac2mon*xmon[2]*(xmon[0]*cosla+xmon[1]*sinla)/rmon**2
    desun = l1*sinphi*(cosphi**2-sinphi**2)*fac2sun*xsun[2]*(xsun[0]*sinla-xsun[1]*cosla)/rsun**2
    demon = l1*sinphi*(cosphi**2-sinphi**2)*fac2mon*xmon[2]*(xmon[0]*sinla-xmon[1]*cosla)/rmon**2
    
    de = 3*(desun+demon)
    dn = 3*(dnsun+dnmon)
    
    xcorsta = [0]*3
    xcorsta[0] = 0
    xcorsta[1] = de
    xcorsta[2] = dn
    xcorsta[0] = -de*sinla-dn*sinphi*cosla
    xcorsta[1] = de*cosla-dn*sinphi*sinla
    xcorsta[2] = dn*cosphi
    
    # compute the station corrections for the diurnal band.
    l1 = l1sd
    costwola = cosla**2-sinla**2
    sintwola = 2.0*cosla*sinla
    
    dnsun = -l1/2*sinphi*cosphi*fac2sun*((xsun[0]**2-xsun[1]**2)*costwola+2*xsun[0]*xsun[1]*sintwola)/rsun**2
    dnmon = -l1/2*sinphi*cosphi*fac2mon*((xmon[0]**2-xmon[1]**2)*costwola+2*xmon[0]*xmon[1]*sintwola)/rmon**2
    desun = -l1/2*sinphi**2*cosphi*fac2sun*((xsun[0]**2-xsun[1]**2)*sintwola-2*xsun[0]*xsun[1]*costwola)/rsun**2
    demon = -l1/2*sinphi**2*cosphi*fac2mon*((xmon[0]**2-xmon[1]**2)*sintwola-2*xmon[0]*xmon[1]*costwola)/rmon**2
    
    de = 3*(desun+demon)
    dn = 3*(dnsun+dnmon)
    
    # compute the diurnal corrections
    xcorsta[0] = xcorsta[0]-de*sinla-dn*sinphi*cosla
    xcorsta[1] = xcorsta[1]+de*cosla-dn*sinphi*sinla
    xcorsta[2] = xcorsta[2]+dn*cosphi
    
    return xcorsta
    
# stepone package
# ====================================================================
