#! /usr/bin/python

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
############################################################################

import os
import shutil
import sys
import time
from PIL import Image
import ImageGrab
import etc.settings as s
from lib.images2gif import writeGif
import msvcrt

img = []
file_location = []
fps = []
time.clock() #reset process timer

program_path = os.path.dirname(sys.argv[0])+'/'
if(os.path.isdir('%stemp'%program_path) is not True): os.mkdir('%stemp'%program_path)
	
raw_input("\nPress enter to start capture.\n")

while(not msvcrt.kbhit()):
	old_time = time.clock()
	img.append(ImageGrab.grab(s.CAPTURE_DIMENSIONS))
	print 'Capturing frame %d'%len(img)
	time.sleep(s.CAPTURE_DELAY)
	fps.append(time.clock()-old_time)

print '\n\n  Captured %d frames in %.3fs'%(len(img), sum(fps))
print '  Frames captured per second: %.2f' %(1/(sum(fps)/len(fps)))
print '\nWriting frames to %s...'%s.GIF_FILE

for x in range(len(img)):
	file_location.append(r'%stemp\frame_%d.jpg'%(program_path,x))
	if(s.RESIZED_DIMENSIONS[0] is not -1): img[x].thumbnail(s.RESIZED_DIMENSIONS, Image.ANTIALIAS) 
	img[x].save(file_location[x])

PILimages = [Image.open(x) for x in file_location]

writeGif(s.GIF_FILE, PILimages, duration = (sum(fps)/len(fps))) #real time framerate
#for filename in file_location: os.remove(filename)
#os.rmdir('temp')
shutil.rmtree('%stemp'%program_path)

print "\n\n\nGIF file information:"
print "  Size:             %d KB" %(os.path.getsize(s.GIF_FILE)/1024)
print "  Frames:           %d" %len(img)
print "  Gif frame rate:   %.1f fps" %(1/(sum(fps)/len(fps)))
print "  Gif duration:     %.3fs\n\n" %(len(img)*(sum(fps)/len(fps)))

time.sleep(8)
