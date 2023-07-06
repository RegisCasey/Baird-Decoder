# Baird Decoder - A small tool to convert audio to images.

***Now on Version 1!***

![image](https://github.com/RegisCasey/Baird-Decoder/assets/138264475/78e010cb-f9df-4e10-a220-addf8d9492cf)


# INTRODUCTION
For those who don't know, the mechanical television was first invented by John Logie Baird in the 1920s. How it worked was that it used a spinning Nipkow disk (a disk with a series of holes spiraling down towards the center) to mimick the raster of an electronic TV, and a flickering light. When the two are put together, you get an image. This program aims to take audio samples from mechanical TV signals, and convert them back into visible images. This program can also decode image audio signals created by the **[Baird Encoder](https://github.com/RegisCasey/Baird-Encoder)** program.

# REQUIREMENTS
**THIS IS A PYTHON SCRIPT, AND AS SUCH, IT IS ASSUMED THAT YOU HAVE AT LEAST PYTHON 3.6.X INSTALLED**

To use this program, you will need to have the [Pillow/PIL](https://pypi.org/project/Pillow/) and [PySoundFile](https://pypi.org/project/PySoundFile/) libraries,  and a Python code editor (Visual Studio Code, [Thonny](https://thonny.org/), etc. installed (all not included).

You will also need a mechanical television signal, which has been provided in this repository to serve as an example.
A text file dump of a signal is also provided.
You can also make your own signals with the [Baird Encoder](https://github.com/RegisCasey/Baird-Encoder) program.

# HOW TO USE
*See the [wiki](https://github.com/RegisCasey/Baird-Decoder/wiki) for documentation on how to use this, it's too extensive for a "README" alone.*

Once you are done, run the script, and once the script is done, it will save the image and display the image the program had created from the
audio samples.

# LIMITATIONS:
- This program can only dump images from audio files, it currently cannot replay the image frames as a video.
- This program does NOT work in real-time; every audio sample must be dumped and loaded into system memory before the program
  can interpretate them as images.
- While the audio used for multi-frame ripping can be whatever (so long as the frame rate is a whole number), **for single frame ripping, the audio must still be 1 second long, and the sample rate must still be (imagewidth x imageheight).**

# TO-DO:
- Test if this program can draw standard definition analog TV signals, such as
the "Voyager Golden Record images".
- Make the program more user-friendly and configurable.
- Add the audio sample rate scaling feature to the single-frame ripping mode as well.
- Implement a "calibration/testing mode" to generate the same image, multiple times, but each with different configurations, to show 

# NOTICES
- You are free to share this program, but you are not allowed to present it as your own creation. If you modify, improve, or integrate the script into your own creations,
  it's kindly requested for me to be included in your credits.

# CHANGELOG

## v1
- First full number release!
- Added support for reading `.wav` audio clips alongside text file dumps.
- Now requires PySoundFile library for reading from `.wav` files.
- Can read and produce multiple images from one audio clip, in a batch sequence. (Versions prior could only do one image per run.)
- Can support almost every sample rate (audio) and framerate (image sequence).
- (Almost) fixed image slanting issue, by adding a toggle (`SlantCorrection`) to enable or disable a correction adjustment. 
- Added values to set directories for inputs and outputs.
- Added basic image processing (Tinting, toning, and levels adjustment.).
- Minor improvements.

## v0.2 - July 3, 2023
- First GitHub release.
- Switched from reading dB values to Linear audio values, allowing for a much cleaner, and more accurate picture reproduction, which still could only be read from sample data export text files from *Audacity*.

![dB-image-rip](https://github.com/RegisCasey/Baird-Decoder/assets/138264475/442ea80a-dc8c-488c-a623-25dd85d32a1a)
![linear-image-rip](https://github.com/RegisCasey/Baird-Decoder/assets/138264475/02c0896a-53de-4314-a76a-2ff91eb57398) 
(Image rights belong to Rebecca Parham/Let Me Explain Studios. Image was used for testing purposes.)

- Added vertical and horizontal offset settings.

## v0.1 (not publicly released)
- Proof of concept.

