# Baird Decoder - Mechanical TV Image Interpreter
# A small project by Regis "Casey" C.
# v1 - July 4, 2023

# You may need to change your Python interpreter to use this script correctly.
# REQUIRES THE PILLOW/PIL AND PYSOUNDFILE PYTHON LIBRARIES

"""

TO-DO:
- Test if this program can draw standard definition analog TV signals, such as
the "Voyager Golden Record images".
- Make the program more user-friendly.

"""

# FILE SETTINGS
# For directory settings, leave blank to use default directories.
# Please format your directory according to your OS, but regardless, ALL
# directories must end with a "/". (/drive/folder/mystuff/ - example.)
inDir = "" # Input audio/text file directory
outDir = "" # Directory to output image rips to.
outName = "OutputImage" # Name of output image file, all rips are saved as bitmap files.
inFile = '' # Name of frame dump, .txt or .wav only.

# CONFIGURATIONS
frame = (0, 0) # Horizontal resolution, vertical resolution
# IF YOUR IMAGE IS ASKEWED, ADJUST THE Y VALUE TO SEE IF THAT CORRECTS IT.
MultiFrame = False # Set to True if your audio/.txt has more than one frame
# Such as a full video clip.
FrameRate = 1 # If dump is a sequence of images (video), how many images exist per second.
# This setting is ignored if MultiFrame is set to "False"

# IMAGE CALIBRATION
VerticalOffset = 0 # Shifts the image up or down
HorizontalOffset = 0 #Shifts the image left or right, may mimick vertOffset?
SlantCorrection = True # Fixes slanting/askew image, leave 'True' by default.
# Set SlantCorrection to 'False' only if slanting is happening with 'True' and
# changing the vertical resolution doesn't fix it.

# CUSTOMIZATION AND IMAGE PROCESSING

TintTone = (0, 0, 0) # Negative values for tint, positive for tone. (R,G,B)
# Tint colors the white areas, tone colors the dark areas.

Levels = False # Set to True to toggle image levels adjustment.
# This setting requires the script to rewrite the ENTIRE image's values, so if your
# audio contains a lot of samples and you have no use for this, leave at "False"
# to avoid reducing processing speed.
highlights = 0
midtones = 0
shadows = 0
# There is no histogram, clipping is very much possible.
# It's only advised to use this in case a correction must be made to the image.

# Coding help from pythontutorial.net and Stack Overflow

from PIL import Image, ImageTk, ImageDraw, ImageMorph
import soundfile as sf
import numpy

pixels = []

if inFile[-4:] == '.txt':
    with open(inFile) as f:
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
elif inFile[-4:] == '.wav': # Dump samples from audio clip.
    SoundInfo = sf.read(inFile)
    Blob, samplerate = sf.read(inFile)
    audDump = numpy.array(SoundInfo).tolist()
    for audList in audDump:
        try:
            for audVal in audList:
                try:
                    print(audVal)
                    pixels.append(audVal)
                except:
                    print('end of dump')
        except:
            print('end of info')
            print(samplerate)

samplerate = samplerate
white = max(pixels) # White point
black = min(pixels) # Black point

print(f'The lowest point is {black}')

print ('done')
# The magic to convert dB values to RGB values is to multiply by -4.
# Make it -8 or -12 for better contrast.
# For "Linear", it is 255, and subtract 164 from brightness
# Linear is being used due to better image reproduction.

def generateFramePalette(dump,multi=False,average=1,framRan=(0,0) ):
    print ('start convert')
    shades = []
    holding = []
    if multi == False:
        for val in dump:
            val = val * -255 # The magic number modifier, also contrast control.
            if val >= 255:
                val == 255 # Caps image values
            val = int(round(val))
            val = 255 - val - 164 # Inverts image to a positive, add/subtract for brightness.
            shades.append(val)
    else:
        loopcount = -1
        print(framRan[0])
        for val in dump[framRan[0]:]:
            if loopcount >= framRan[1]:
                break
            else:
                val = val * -255 # The magic number modifier, also contrast control.
                if val >= 255:
                    val == 255 # Caps image values
                val = int(round(val))
                val = 255 - val - 164 # Inverts image to a positive, add/subtract for brightness.
                holding.append(val)
                if len(holding) >= average: # Downscales audio image to correct resolution,
                    simpToy = holding[0] # to easily get 32x34 (1088hz) images from 44100hz audio for example.
                    shades.append(simpToy)
                    holding = []
                loopcount += 1
    print(shades)
    return shades

def scaleToFPS(samplerate, pixelArea, FPS=1): # Equation to calculate how much needs to
    ratePerFrame = samplerate/FPS # be averaged out to convert audios to a correct
    toAverage = ratePerFrame/pixelArea # sample rate.
    return toAverage

def downscaleAudio(dump,average=1): # Unused, may be removed in later versions.
    holding = []
    pixels2 = []
    for toy in dump:
        if len(holding) >= average:
            simpToy = holding[0]
            pixels2.append(simpToy)
            holding = []
        holding.append(toy)
    return pixels2

# Drawing the image from the values.

FramePixelCount = frame[0]*frame[1]


if MultiFrame == True:
    loopcount = 0
    startingPixel = 0
    toAverage = scaleToFPS(samplerate,FramePixelCount,FrameRate) # Calculates value to average out sample rates by.
    #pixels2 = downscaleAudio(pixels, toAverage)
    FramePixelCount *= toAverage # "To get a 1088hz image from a 12fps 44100hz file, we need to upscale to 3674hz"
    FramePixelCount = int(round(FramePixelCount))
    looptotal = len(pixels)/FramePixelCount # Calculates how much to loop the drawing script (goes by per frame)
    looptotal = int(round(looptotal))
    while loopcount != looptotal:
        FrameConvert = Image.new('RGB',(frame))
        PixColor = FrameConvert.load()
        Pixie = PixColor

        PixelVal = generateFramePalette(pixels,True,toAverage,(startingPixel, FramePixelCount))
        horizCount = 0 + HorizontalOffset # Adjusting either value offsets the image.
        vertCount = 0 + VerticalOffset
        if Levels == True:
            PixTemp = []
            for RGBval in PixelVal:
                if RGBval >= 170:
                    RGBval += highlights
                if RGBval >= 86 and RGBval <= 169:
                    RGBval += midtones
                if RGBval <= 85:
                    RGBval += shadows
                PixTemp.append(RGBval)
            PixelVal = PixTemp
                
        if SlantCorrection == True:
            SlantCorrection = -1
        for n in range(frame[0]+SlantCorrection):
            horizCount += 1  
            for m in range(frame[1]+SlantCorrection): # Fixes askew bug as best as it can
                vertCount += 1 
                try:
                    PixColor[n,m] = (PixelVal[horizCount+vertCount]+TintTone[0], PixelVal[horizCount+vertCount]+TintTone[1], PixelVal[horizCount+vertCount]+TintTone[2])
                except:
                    print('That is all')
                    print(toAverage)
                    print(startingPixel)
                    
        #FrameConvert.show()
        FrameConvert.save(f"{outDir}{outName}-{loopcount}.bmp")
        startingPixel += FramePixelCount # "Hey artist, start counting the values from 1001 after counting up to 1000."
        loopcount += 1
else: # This one is simpler because it focuses on only drawing 1 frame.
    FrameConvert = Image.new('RGB',(frame))
    PixColor = FrameConvert.load()
    Pixie = PixColor

    PixelVal = generateFramePalette(pixels)
    horizCount = 0 + HorizontalOffset # Adjusting either value offsets the image.
    vertCount = 0 + VerticalOffset
    if Levels == True:
        PixTemp = []
        for RGBval in PixelVal:
            if RGBval >= 170:
                RGBval += highlights
            if RGBval >= 86 and RGBval <= 169:
                RGBval += midtones
            if RGBval <= 85:
                RGBval += shadows
            PixTemp.append(RGBval)
        PixelVal = PixTemp

    if SlantCorrection == True:
            SlantCorrection = -1
    for n in range(frame[0]+SlantCorrection):
        horizCount += 1  
        for m in range(frame[1]+SlantCorrection): # Fixes askew bug as best as it can
            vertCount += 1 
            try:
                PixColor[n,m] = (PixelVal[horizCount+vertCount]+TintTone[0], PixelVal[horizCount+vertCount]+TintTone[1], PixelVal[horizCount+vertCount]+TintTone[2])
            except:
                print('That is all')
                
    FrameConvert.show()
    FrameConvert.save(f"{outDir}{outName}.bmp")
