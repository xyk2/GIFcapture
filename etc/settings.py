# List of variables used in the main program.


#Set the name and path of the saved gif. Include the .gif extension.
GIF_FILE = 'animation.gif'

#Coordinates for the captured area. Format is [x0, y0, x1, y1].
#Like all computer graphic systems, the origin is at the top-left corner of the screen.
CAPTURE_DIMENSIONS = [10, 150, 970, 680]

#Resized dimensions. Every frame that is not resized will be around ~1MB, so it is highly recommended to do so.
#Format is [width, height] in pixels. If resize is not required, set the first item to -1.
RESIZED_DIMENSIONS = [320, 178]

#Delay between screen captures in seconds. The maximum speed is approximately 20fps, or 50 milliseconds between captures.
#Eventually this will be integrated into a 'Select capture fps' input.
#Note that this time is IN ADDITION to the ~50ms capture overhead.
CAPTURE_DELAY = 0.0