# Baird-Decoder

HOW TO CONVERT YOUR MECHANICAL TV SIGNALS
INTO A FRAME DUMP TEXT FILE FOR THE INTERPRETER:

- Determine the resolution of the video (example 32 x 34)
- Multiply the two numbers (32 x 24 = 1088 for instance)
- Remember that number.
- Open your TV audio file in Audacity
- Select a singular frame of the signal, and copy it.
- Open a new Audacity file and paste the frame in there.
- On the timeline, click on the audio name, and change the
sample rate to the number you got from multiplying the
resolutons (1088hz for example)
	Hint: You might need to change the sample rate to a 
	preset before you can put in a custom one.
- (Optional) If you're not getting desired results,
go to EFFECT > CHANGE SPEED, and set the "New Length" to 1 sec.
- Once that is done, click on ANALYZE > SAMPLE DATA EXPORT
- Now make sure your settings are as followed:
  
	Limit output to first: (Your multiplied number)
	Meaurement scale: Linear
	File data format: Sample List (txt)
	Include header information: None
	Optional header text: (Leave blank)
	Channel layout for stereo: L Channel First
	Show messages: None
	File name: (Something distinguishable)
	Output folder: (Where you can find it)

