#!/usr/bin/env python
"""
img2gcode.py
functions for digesting paths into a simple list structure

Copyright (C) 2014 Teja Philipp, teja@mr-beam.org

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
import re, math

def base64toFile(s, file="/tmp/mrbeam_webinterface_tmp.png"):
    fh = open(file, "wb")
    fh.write(s.decode('base64'))
    fh.close()

def imgPrepare(path, w,h, material):
    """
    1.pixel reduction (w,h)
    2.greyscale
	3.contrast / curves (material)
    """
    # read image 
    # pythonMagick scale
    # pythonMagick greyscale
    # pythonMagick curves
    # pythonMagick mirror?
    # return pixel array
	
def toGcode(pixelArray, x,y, minIntensity, maxIntensity):
    # iterate line by line
    # back and forth
    # combine equal values
    # return gcode
	return



# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 encoding=utf-8 textwidth=99
