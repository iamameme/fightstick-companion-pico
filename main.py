from time import sleep
from ili9341 import Display
from machine import Pin, SPI
from wavePlayer import wavePlayer
import _thread
from xpt2046 import Touch

## Variables to alter
raw_images_file_name = "deejay"
audio_file_name = "val.wav"

SCK_PIN_DISPLAY = 6
MOSI_PIN_DISPLAY = 7
DC_PIN_DISPLAY = 15
CS_PIN_DISPLAY = 13
RST_PIN_DISPLAY = 14

SCK_PIN_TOUCH = 10
MOSI_PIN_TOUCH = 11
MISO_PIN_TOUCH = 8
CS_PIN_TOUCH = 12

SPI_CHANNEL_DISPLAY = 0
SPI_CHANNEL_TOUCH = 1

# These aren't actually passed into wavePlayer, but could be (these are the default values)
AUDIO_LEFT_PIN = 2
AUDIO_RIGHT_PIN = 3
VIRTUAL_GND_PIN = 4
 
# Initialize the SPI interfaces (display,touch) and audio
spi = SPI(SPI_CHANNEL_DISPLAY, baudrate=40000000, sck=Pin(SCK_PIN_DISPLAY), mosi=Pin(MOSI_PIN_DISPLAY))
display = Display(spi, dc=Pin(DC_PIN_DISPLAY), cs=Pin(CS_PIN_DISPLAY), rst=Pin(RST_PIN_DISPLAY))

spi2 = SPI(SPI_CHANNEL_TOUCH, baudrate=1000000, sck=Pin(SCK_PIN_TOUCH), mosi=Pin(MISO_PIN_TOUCH), miso=Pin(MISO_PIN_TOUCH))
touch = Touch(spi2, cs=Pin(CS_PIN_TOUCH))

player = wavePlayer()
file = player.open_file(audio_file_name)

def play_audio():
    try:
        player.play(file)
    except OSError as exc:
        print(exc)
        if exc != 20:
            print("EXECUTING FALLBACK PLAN")
            count = 0
            try:
                player.stop()
                player.play(file)
                player.stop()
            except:
                print("try again")
            try:
                print("gave up")
                player.stop()
                count = 0
                file.rewind()
            except:
                print("tried to stop nothing")
        
def get_a_touch():
    ret = touch.get_touch()
    if ret is not None:
        print(ret)
        try:
            _thread.start_new_thread(play_audio, ())
        except:
            print("core in use but thats fine")
    return

def main():
    # Baud rate of 40000000 seems about the max
    # Play the audio on power on
    _thread.start_new_thread(play_audio, ())
    while True:
        for i in range(7):
            try:
                display.draw_image(raw_images_file_name + str(i) + '.raw', 0, 0, 240, 320)
            except:
                print("print failed :(")
            get_a_touch()
            sleep(.01)
        for i in reversed(range(6)):
            try:
                display.draw_image(raw_images_file_name + str(i) + '.raw', 0, 0, 240, 320 )
            except:
                print("print failed :(")
            sleep(.01)
            get_a_touch()

main()


