#!/usr/bin/ruby

left = nil
right = nil
top = nil
bottom = nil
ARGF.each do |line|
	if line.match(/^G0?[0,1,2,3]/) != nil then

	  x = /X(\d+[.]?\d+)/.match line 
	  left = [left, x[1].to_f].compact.min unless x == nil
	  right = [right, x[1].to_f].compact.max unless x == nil

	  y = /Y(\d+)/.match line    
	  top = [top, y[1].to_f].compact.max unless y == nil
	  bottom = [bottom, y[1].to_f].compact.min unless y == nil

	end
end

w = right - left
h = top - bottom

puts "bounding box: [" + [left, bottom, ',', right, top].join(' ') + "] mm"
puts "dimensions " + [w, h].join( '*') + " mm"


