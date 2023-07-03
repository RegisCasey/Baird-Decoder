# Baird-Decoder

# INTRODUCTION
For those who don't know, the mechanical television was first invented by John Logie Baird in the 1920s. How it worked was that it used a spinning Nipkow disk (a disk with a series of holes spiraling down towards the center) to mimick the raster of an electronic TV, and a flickering light. When the two are put together, you get an image. This program aims to take audio samples from mechanical TV signals, and convert them back into visible images. This program can also decode image audio signals created by the **Baird Encoder** program.

# REQUIREMENTS
**THIS IS A PYTHON SCRIPT, AND AS SUCH, IT IS ASSUMED THAT YOU HAVE AT LEAST PYTHON 3.6.X INSTALLED**

To use this program, you will need to have the [Pillow/PIL](https://pypi.org/project/Pillow/) library and a Python code editor
(Visual Studio Code, [Thonny](https://www.Thonny.org/), etc.) installed (both not included).

You will also need a mechanical television signal, which has been provided in this repository to serve as an example.
You can also make your own with the Baird Encoder program.

# HOW TO USE
Open the `BairdDecoder-v0.2-RegisC.py` script in a code editor, and modify the values listed in **MAIN CONFIGURATIONS**.
Once you are done, run the script, and once the script is done, it will save the image and display the image the program had created from the
audio samples.

# MAIN CONFIGURATIONS
`frame = (x,y)` - Horizontal resolution, vertical resolution.
**IF YOUR OUTPUT IMAGE IS ASKEWED/TILTED, ADJUST THE Y VALUE TO SEE IF THAT CORRECTS IT.**

`outName` - Name of image file, all rips are saved as bitmap (`.bmp`) files.

`DumpTxt` - Name of frame dump .txt file. **Please include the .txt extension.**

`VerticalOffset` - Shifts the image up or down

`HorizontalOffset` = Shifts the image left or right

# PICTURE CONTROL
**It is not advised to modify these values. Do not report bugs if you modify these values.**

In the script, you are going to look for `def generateFramePalette(dump):`. In the `for val in dump:` loop, you will find two
lines that can be modified to adjust how the program processes images.

- `val = val * -255` - This converts the audio value to an RGB value, but "-255" can be modified to adjust the image **contrast**.
-  `val = 255 - val - 164` - This inverts the image to a positive, but "164" can be modified to adjust the image **brightness**.

**There should be no reason for these values to be changed.** The script was calibrated to ensure the most accurate image reproduction
based on my testing, I'm only mentioning this for debugging purposes.


# HOW TO CONVERT YOUR MECHANICAL TV SIGNALS INTO A FRAME DUMP TEXT FILE FOR THE INTERPRETER:
*Requires [Audacity](https://www.audacityteam.org/) (not included)*

- Determine the resolution of the video (example 32 x 34)
- Multiply the two numbers (32 x 24 = 1088 for instance)
- Remember that number.
- Open your TV audio file in Audacity
- Select a singular frame of the signal, and copy it.
  (Frames look like a repeating pattern in the waveform)
- Open a new Audacity file and paste the frame in there.
- On the timeline, click on the audio name, and change the
sample rate to the number you got from multiplying the
resolutons (1088hz for example)
	Hint: You might need to change the sample rate to a 
	preset before you can put in a custom one.
- (Optional) If you're not getting desired results,
go to `EFFECT > CHANGE SPEED`, and set the "New Length" to 1 sec.
- Once that is done, click on `ANALYZE > SAMPLE DATA EXPORT`
- Now make sure your settings are as followed:

  	`Limit output to first: (Your multiplied number)`
  
	`Meaurement scale: Linear`

	`File data format: Sample List (txt)`

	`Include header information: None

	`Optional header text: (Leave blank)`

	`Channel layout for stereo: L Channel First`

	`Show messages: None`

	`File name: (Something distinguishable)`

	`Output folder: (Where you can find it)`

# LIMITATIONS:
- This program can only convert individual frames into a visible image.
- This program cannot rip data from audio files; you must provide a text file
sample data export of a SINGULAR FRAME of the mechanical TV signal, as explained in this `README` file
- This program only draws out an image from audio, only image controls you are given are brightness and contrast control.

# TO-DO:
- Test if this program can draw standard definition analog TV signals, such as
the "Voyager Golden Record images".
- Make the program more user-friendly and configurable.
- Have the program able to read from .wav files directly

# NOTICES
- You are free to share this program, but you are not allowed to present it as your own creation. If you modify, improve, or integrate the script into your own creations,
  it's kindly requested for me to be included in your credits.
