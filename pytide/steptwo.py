#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Changfu Chen, Southwest Jiaotong University
# August 01, 2017
# 

from math import *
from datetime import *

# ====================================================================
# steptwo package
# --------------------------------------------------------------------
# Subroutine: Gives the in-phase and out-of-phase corrections induced 
#     by mantle anelasticity in the diurnal band.
# --------------------------------------------------------------------
def step2diu(xsta,fhr,t):
    # Function：
    #         Gives the in-phase and out-of-phase corrections induced 
    #         by mantle anelasticity in the diurnal band.
    # Input:
    #         xsta: Geocentric position of the IGS station
    #         fhr: Fractional hours in the day
    #         t: Centuries since J2000
    # Output:
    #         xcorsta: in-phase and out-of-phase corrections for diurnal band
    # Example:
    #         xsta = [4075578.385,931852.890,4801570.154];
    #         fhr = 0;
    #         t = 0.1059411362080767;
    # Results:
    #         xcorsta = [0.4193085327321284701E-02,0.1456681241014607395E-02,0.5123366597450316508E-02];
    
    datdi = [[-3,-3,-2,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,2,2,3,3], \
             [0,2,0,0,2,0,0,2,-2,0,0,0,2,-3,-2,-2,-1,-1,0,0,0,0,1,1,1,2,2,-2,0,0,0], \
             [2,0,1,1,-1,0,0,0,1,-1,1,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,1,-1,0,0], \
             [0,0,-1,0,0,-1,0,0,0,0,0,1,0,0,-1,0,0,0,-1,0,1,2,0,0,1,0,0,0,0,0,1], \
             [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,-1,1,0,0,0,0,-1,1,-1,0,0,0,0,0,0], 
             [-0.01,-0.01,-0.02,-0.08,-0.02,-0.1,-0.51,0.01,0.01,0.02,0.06,0.01,0.01, \
              -0.06,0.01,-1.23,0.02,0.04,-0.22,12,1.73,-0.04,-0.5,0.01,-0.01,-0.01,-0.11,-0.01,-0.02,0,0], \
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-0.07,0,0,0.01,-0.8,-0.12,0,-0.01,0,0,0,0.01,0,0,0,0], \
             [0,0,0,-0.01,0,0,-0.02,0,0,0,0,0,0,0,0,0.06,0,0,0.01,-0.67,-0.1,0,0.03,0,0,0,0.01,0,0,0,0], \
             [0,0,0,0.01,0,0,0.03,0,0,0,0,0,0,0,0,0.01,0,0,0,-0.03,0,0,0,0,0,0,0,0,0,0,0]]
    deg2rad = 2*pi/360
    
    # compute the phase angles in degrees
    s = 218.31664563 \
        + (481267.88194 \
        + (-0.0014663889 \
        + (0.00000185139)*t)*t)*t
    
    tau = fhr*15 \
        + 280.4606184 \
        + (36000.7700536 \
        + (0.00038793 \
        + (-0.0000000258)*t)*t)*t \
        + (-s)
    
    pr = (1.396971278 \
        + (0.000308889 \
        + (0.000000021 \
        + (0.000000007)*t)*t)*t)*t
    
    s = s + pr
    
    h = 280.46645 \
        + (36000.7697489 \
        + (0.00030322222 \
        + (0.000000020 \
        + (-0.00000000654)*t)*t)*t)*t
    
    p = 83.35324312 \
        + (4069.01363525 \
        + (-0.01032172222 \
        + (-0.0000124991 \
        + (0.00000005263)*t)*t)*t)*t
    
    zns = 234.95544499 \
        + (1934.13626197 \
        + (-0.00207561111 \
        + (-0.00000213944 \
        + (0.00000001650)*t)*t)*t)*t
    
    ps = 282.93734098 \
        + (1.71945766667 \
        + (0.00045688889 \
        + (-0.00000001778 \
        + (-0.00000000334)*t)*t)*t)*t
    
    # reduce angles to between the range 0 and 360
    s   = s   % 360
    tau = tau % 360
    h   = h   % 360
    p   = p   % 360
    zns = zns % 360
    ps  = ps  % 360
    
    # the normalized position vector
    rsta   = sqrt(xsta[0]**2+xsta[1]**2+xsta[2]**2)
    sinphi = xsta[2]/rsta
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    cosla  = xsta[0]/cosphi/rsta
    sinla  = xsta[1]/cosphi/rsta
    zla    = atan(xsta[1]/xsta[0])
    
    xcorsta = [0]*3
    for j in range(1,32):
        thetaf = (tau+datdi[0][j-1]*s+datdi[1][j-1]*h+datdi[2][j-1]*p+datdi[3][j-1]*zns+datdi[4][j-1]*ps)*deg2rad
        dr = datdi[5][j-1]*2*sinphi*cosphi*sin(thetaf+zla)+datdi[6][j-1]*2*sinphi*cosphi*cos(thetaf+zla)
        dn = datdi[7][j-1]*(cosphi**2-sinphi**2)*sin(thetaf+zla)+datdi[8][j-1]*(cosphi**2-sinphi**2)*cos(thetaf+zla)
        de = datdi[7][j-1]*sinphi*cos(thetaf+zla)-datdi[8][j-1]*sinphi*sin(thetaf+zla)
    
        # compute the diurnal corrections
        xcorsta[0] = xcorsta[0]+dr*cosla*cosphi-de*sinla-dn*sinphi*cosla
        xcorsta[1] = xcorsta[1]+dr*sinla*cosphi+de*cosla-dn*sinphi*sinla
        xcorsta[2] = xcorsta[2]+dr*sinphi+dn*cosphi
    
    
    xcorsta = [i/j for i,j in zip(xcorsta, [1000]*3)]
    return xcorsta
    
# --------------------------------------------------------------------
# Subroutine: Gives the in-phase and out-of-phase corrections induced 
#     by mantle anelasticity in the long-period band.
# --------------------------------------------------------------------
def step2lon(xsta,t):
    # Function：
    #         Gives the in-phase and out-of-phase corrections induced 
    #         by mantle anelasticity in the long-period band.
    # Input:
    #         xsta: Geocentric position of the IGS station
    #         t: Centuries since J2000
    # Output:
    #         xcorsta: in-phase and out-of-phase corrections for diurnal band
    # Example:
    #         xsta = [4075578.385,931852.890,4801570.154];
    #         t    = 0.1059411362080767;
    # Results:
    #         xcorsta = [-0.9780962849562107762E-04,-0.2236349699932734273E-04,0.3561945821351565926E-03];
    
    datdi = [[0,0,1,2,2], \
             [0,2,0,0,0], \
             [0,0,-1,0,0], \
             [1,0,0,0,1], \
             [0,0,0,0,0],\
             [0.470,-0.200,-0.110,-0.130,-0.0500], \
             [0.230,-0.120,-0.0800,-0.110,-0.0500], \
             [0.160,-0.110,-0.0900,-0.150,-0.0600], \
             [0.0700,-0.0500,-0.0400,-0.0700,-0.0300]]
    deg2rad = 2*pi/360
    
    # compute the phase angles in degrees
    s = 218.31664563 \
        + (481267.88194 \
        + (-0.0014663889 \
        + (0.00000185139)*t)*t)*t
    
    pr = (1.396971278 \
        + (0.000308889 \
        + (0.000000021 \
        + (0.000000007)*t)*t)*t)*t
    
    s = s + pr
    
    h = 280.46645 \
        + (36000.7697489 \
        + (0.00030322222 \
        + (0.000000020 \
        + (-0.00000000654)*t)*t)*t)*t
    
    p = 83.35324312 \
        + (4069.01363525 \
        + (-0.01032172222 \
        + (-0.0000124991 \
        + (0.00000005263)*t)*t)*t)*t
    
    zns = 234.95544499 \
        + (1934.13626197 \
        + (-0.00207561111 \
        + (-0.00000213944 \
        + (0.00000001650)*t)*t)*t)*t
    
    ps = 282.93734098 \
        + (1.71945766667 \
        + (0.00045688889 \
        + (-0.00000001778 \
        + (-0.00000000334)*t)*t)*t)*t
    
    # reduce angles to between the range 0 and 360
    s   = s   % 360
    h   = h   % 360
    p   = p   % 360
    zns = zns % 360
    ps  = ps  % 360
    
    rsta   = sqrt(xsta[0]**2+xsta[1]**2+xsta[2]**2)
    sinphi = xsta[2]/rsta
    cosphi = sqrt(xsta[0]**2+xsta[1]**2)/rsta
    cosla  = xsta[0]/cosphi/rsta
    sinla  = xsta[1]/cosphi/rsta
    
    dr_tot = 0
    dn_tot = 0
    xcorsta = [0]*3
    for j in range(1,6):
        thetaf = (datdi[0][j-1]*s+datdi[1][j-1]*h+datdi[2][j-1]*p+datdi[3][j-1]*zns+datdi[4][j-1]*ps)*deg2rad
        dr = datdi[5][j-1]*(3*sinphi**2-1)/2*cos(thetaf)+datdi[7][j-1]*(3*sinphi**2-1)/2*sin(thetaf)
        dn = datdi[6][j-1]*(cosphi*sinphi*2)*cos(thetaf)+datdi[8][j-1]*(cosphi*sinphi*2)*sin(thetaf)
        
        de = 0
        dr_tot = dr_tot+dr
        dn_tot = dn_tot+dn
        
        # compute the diurnal corrections
        xcorsta[0] = xcorsta[0]+dr*cosla*cosphi-de*sinla-dn*sinphi*cosla
        xcorsta[1] = xcorsta[1]+dr*sinla*cosphi+de*cosla-dn*sinphi*sinla
        xcorsta[2] = xcorsta[2]+dr*sinphi+dn*cosphi
    
    xcorsta = [i/j for i,j in zip(xcorsta, [1000]*3)]
    return xcorsta
    
# steptwo package
# ====================================================================
