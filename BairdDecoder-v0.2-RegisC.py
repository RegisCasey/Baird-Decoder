# Baird Decoder - Mechanical TV Image Interpreter
# A small project by Regis "Casey" C.
# v0.2 - July 3, 2023

# You may need to change your Python interpreter to use this script correctly.
# REQUIRES THE PILLOW/PIL PYTHON LIBRARY

"""
LIMITATIONS:
- This program can only convert individual frames into a visible image.
- This program cannot rip data from audio files; you must provide a text file
sample data export of a SINGULAR FRAME of the mechanical TV signal.
- See ReadMe.txt for info on dumping your own frame files.

TO-DO:
- Test if this program can draw standard definition analog TV signals, such as
the "Voyager Golden Record images".
- Make the program more user-friendly and configurable.
- Have the program able to read from .wav files directly.

"""

# CONFIGURATIONS
frame = (64, 67) # Horizontal resolution, vertical resolution
# IF YOUR IMAGE IS ASKEWED, ADJUST THE Y VALUE TO SEE IF THAT CORRECTS IT.
outName = "SampleBuild" # Name of image file, all rips are saved as bitmap files.
DumpTxt = 'SampleDump.txt' # Name of frame dump .txt file.
VerticalOffset = 0 # Shifts the image up or down
HorizontalOffset = 0 #shifts the image left or right

# Coding help from pythontutorial.net and Stack Overflow


import fractions
from PIL import Image, ImageDraw, ImageMorph
import soundfile as sf

pixels = []

with open(DumpTxt) as f:
    while True:
        line = f.readline()
        values = line.strip()
        try:
            pixels.append(float(values)) # Converts the audio samples into
                                        # floating point numbers
        except:
            print("This string cannot be made into a float.")
        if not line:
            break
        print(line.strip())
    print (pixels)

f.close()

sf.write('TEstrecord.wav', pixels, 44100, 'PCM_24')

white = max(pixels) # White point
black = min(pixels) # Black point

print(f'The lowest point is {black}')

print ('done')
# The magic to convert dB values to RGB values is to multiply by -4.
# Make it -8 or -12 for better contrast.
# For "Linear", it is 255, and subtract 164 from brightness
# Linear is being used due to better image reproduction.

def generateFramePalette(dump):
    print ('start convert')
    shades = []
    for val in dump:
        val = val * -255 # The magic number modifier, also contrast control.
        if val >= 255:
            val == 255 # Caps image values
        val = int(round(val))
        val = 255 - val - 164 # Inverts image to a positive, add/subtract for brightness.
        shades.append(val)
    print(shades)
    return shades


# Drawing the image from the values.

FrameConvert = Image.new('RGB',(frame))
PixColor = FrameConvert.load()
Pixie = PixColor

PixelVal = generateFramePalette(pixels)
horizCount = 0 + HorizontalOffset # Adjusting either value offsets the image.
vertCount = -1 + VerticalOffset # -1 by default to fix minor bug.
for n in range(frame[0]):
    horizCount += 1
    for m in range(frame[1]):
        vertCount += 1
        try: # Slanting is caused by script drawing starting at the 3rd pixel.
            PixColor[n,m] = (PixelVal[horizCount+vertCount], PixelVal[horizCount+vertCount], PixelVal[horizCount+vertCount])
        except:
            print('That is all')
            
FrameConvert.show()
FrameConvert.save(f"{outName}.bmp")
