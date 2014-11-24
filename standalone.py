#!/usr/bin/env python

import sys
from mrbeam import Laserengraver

conv = Laserengraver()

infile = None
outfile = None

# get the svg input file name from the commandl line params
# try:
	# infile = sys.argv[-1]
# except:
	# print "Please provide an input SVG file"
	# print "Usage standalone.py INPUT"
	# sys.exit()

# outfile = "%s.gcode" % infile.replace(".svg","")
	
# conv.options.directory = "/Users/philipp/Desktop"
# conv.options.file = "test.gcode"
# self.options.active_tab = "Laser"
	
# create the SVG element tree
# conv.parse()

# and apply the effect
conv.affect()

