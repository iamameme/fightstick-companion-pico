# Fightstick Companion 

- This code makes your Pi Pico play a GIF and play audio on touch of a touchscreen
- Not really related to this but, my use-case was to attach this to my fight stick 
- By attaching your Pico to the VCC_5V and GRD on your Brook fight board (I used a Brook Zero Pi), it runs off the USB connection!
- I don't really know if you could use something more powerful, but I was trying to use as little power as possible, so we REALLY push the limits of the Pico
- But it works

# Make image files for screen

- For an image, use `python img2rgb565.py <filename>`
- For a gif, use `python gif2raw.py <filename> <frameno>`
- For cropping gifs to screen size, I used: https://ezgif.com/crop

They are located in helper_functions folder

# Parts Used

- Raspberry Pi Pico
- 3W Speaker
- ili9341 Driven Display (Others probably work, but the cheap Waveshare ones are that driver) w/ TouchScreen
- 2.5W Amp (Any amp works)
- UNRELATED: Brook Zero Pi Fight Board

Total Cost: ~$40 + Fight Board

# Exact Parts

- Screen: https://www.amazon.com/dp/B0BF5G8ZQJ?psc=1&ref=ppx_yo2ov_dt_b_product_details
- Pico: https://www.amazon.com/dp/B0B1CD8SPS?psc=1&ref=ppx_yo2ov_dt_b_product_details
- Speaker: https://www.amazon.com/dp/B01CHYIU26?psc=1&ref=ppx_yo2ov_dt_b_product_details
- Amp: https://www.amazon.com/dp/B00PY2YSI4?psc=1&ref=ppx_yo2ov_dt_b_product_details
- Fight Board: https://www.amazon.com/Brook-Zero-Fighting-Board-Version/dp/B09637ZPSF/ref=sr_1_8?crid=144J7CCWFRFGZ&keywords=zero+pi&qid=1690801038&sprefix=zero+p%2Caps%2C170&sr=8-8

Yes everything is from amazon; don't do the same. It's cheaper elsewhere and you can support local online businesses.

# Test with examples

- In the examples folder, there is an audio folder with a wav file, place that on your pico
- Inside of examples, there is also an images folder, with a couple examples
	- Place the .raw files from one of those folders onto the pico
- Alter main.py with the file names of your wav/raw files
- Put all files in the root of this project onto your pico (`chunk.py`, `ili9341.py`, etc.)
- Change all the pins in `main.py` to account for where your things are plugged in 

# Notes

- Audio is pre-programmed to be on GPIO Pin 3/4 (Only one of them worked for me)
- My amp has two outs (R/L), but since it's Mono, ground the unused one
- The audio runs into OSError: 84 sometimes (and 20), so some try/catch loops catch it
	- This means that the audio will sometimes just stop, but it can be restarted
	- If someone wants to fix this, please do 
- Space is an issue, so I realized that 7 320x240 images and one wav file was the limit
	- An aftermarket Pico with more storage will enable longer gifs / more audio files
	
# Code that I didn't write

- WavePlayer for Pico (https://github.com/danjperron/PicoAudioPWM)
	- `wavePlayer.py`, `myDMA.py`, `myPWM.py`
- Audio libs from (https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio)
	- `wave.py` and `chunk.py`
- Display / touch drivers from (https://github.com/rdagger/micropython-ili9341)
	- `ili9341.py`, `xpt2046.py`
- I would say to download them directly from there, but there are tiny edits to them so idk what to do