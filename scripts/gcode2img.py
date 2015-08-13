# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "teja"
__date__ = "$Aug 9, 2015 9:42:03 AM$"

import optparse
import os.path
from PIL import Image

def debug_image(gcode, pixelsize):
	import string, sys, re
	lines = string.split(gcode, '\n')
	xmin = sys.maxint
	xmax = -sys.maxint
	ymin = sys.maxint
	ymax = -sys.maxint
	fmin = sys.maxint
	fmax = -sys.maxint
	regex = re.compile("((?P<letter>[GFSMXYZPIJK])\s*(?P<value>[0-9-.]+))")

	x = 0
	y = 0
	s = 0
	f = 0
	g = 0
	ltr = True
	pix = []
	for line in lines:
		#matches = regex.findall(line)
		for d in [matches.groupdict() for matches in regex.finditer(line)]:

			if(d['letter'] == 'G'):
				g = d['value']

			if(d['letter'] == 'S'):
				s = float(d['value'])

			if(d['letter'] == 'F'):
				f = float(d['value'])
				fmin = min(f, fmin)
				fmax = max(f, fmax)

			if(d['letter'] == 'X'):
				tmp_x = float(d['value'])
				ltr = tmp_x > x
				x = tmp_x
				xmin = min(x, xmin)
				xmax = max(x, xmax)

			if(d['letter'] == 'Y'):
				y = float(d['value'])
				ymin = min(y, ymin)
				ymax = max(y, ymax)

		pix.append({'g':g, 'x':x, 'y':y, 's':s, 'f':f, 'ltr': ltr})

	h = int((ymax - ymin) * 1/pixelsize) + 1
	w = int((xmax - xmin) * 1/pixelsize) + 2
	f_factor = 1/fmax

	
	print("Gcode (mm): {:.2f}x{:.2f} @ {:.2f},{:.2f}".format(xmax-xmin, ymax-ymin, xmin, ymin) )
	print("Image (px): {:.2f}x{:.2f} @ {:.2f},{:.2f}".format(w, h, xmin * 1/pixelsize, ymin * 1/pixelsize) )


	img = Image.new("L", (w*2,h), "white")
	pixarray = img.load()
	last_px = None;
	for line in pix:
		if(line['g'] == '1' or line['g'] == '0'):
			x = int((line['x']-xmin) * 1/pixelsize)
			if(line['ltr']):
				#x = x-1
				pass
			y = h-1 - (line['y'] - ymin) * 1/pixelsize
			print(y, line)
			if(line['g'] == '1'):
				s = int((1-line['s'] / 1000.0) * 255) # intensity (0-1000) to luminance conversion
				f = (line['f'] * f_factor) * 255
				if(last_px != None):
					_min = min(last_px[0], x)
					_max = max(last_px[0], x)
					if(_min == _max):
						pixarray[x, y] = s
						pixarray[x+w, y] = f
					else:
						x_range = range(_min, _max)
						for px in x_range:
							pixarray[px, y] = s
							pixarray[px+w, y] = f
			last_px = [x,y]
	return img	
	
if __name__ == "__main__":
	opts = optparse.OptionParser(usage="usage: %prog <gcodefile> [<imagefile>]")
	(options, args) = opts.parse_args()

	
	if(len(args) < 1 or len(args) > 2):
		print("usage: gcode2img.py <gcodefile> [<imagefile>]")
		exit(1)
		
	gcodefile = args[0]
	if(len(args) == 2):
		imagefile = args[1]
	else:
		filename, _ = os.path.splitext(gcodefile)
		imagefile = filename + ".png"
		
	with open (gcodefile, "r") as f:
		gcode = f.read()
	img = debug_image(gcode, 0.25)
	img.save(imagefile)

	print("written image " + imagefile)
	exit(0)