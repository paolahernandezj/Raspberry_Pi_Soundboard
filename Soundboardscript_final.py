from gpiozero import Button, LED
import pygame.mixer
from pygame.mixer import Sound
from signal import pause
import time

#this is a comment
pygame.init()
pygame.mixer.init()
SOUND_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(SOUND_END)
isPlaying = False;
current_sound_button_object = -1

objs = [

{ "buttonPin" : 24, "ledPin" : 17, "soundFile":
"/home/pi/desktop/wolves.wav"},

]

class SoundButton:

       def __init__(self, id, button_pin, led_pin, sound_file):
               self.id = id
               self.button_pin = button_pin
               self.led_pin = led_pin
               self.sound_file = sound_file
               self.sound = Sound(sound_file)

               self.button = Button(button_pin)
               self.led = LED(led_pin)
               self.led.off()

               print(self.button_pin)
               
               self.button.when_pressed = self.pressed

       def pressed(self):
               print("pressed")
               pygame.mixer.music.load(self.sound_file)
               pygame.mixer.music.play()
	       soundButtons [current_sound_button_object].turn_off_led()
               self.led.on()
	       current_sound_button_object = self.id
	       
       def turn_off_led(self):
               self.led.off()



soundButtons = []


for index, item in enumerate(objs):
       sb = SoundButton(index, item["buttonPin"], item["ledPin"], item["soundFile"])
       soundButtons.append(sb) """this section of the code defines which--
                               items will be affected when the code is running"""

for button in soundButtons:
   button.led.on()
   print 'led on'
   time.sleep(0.15) #defines how long the LED light will turn on for after it was ran (.15 of a second)

for button in soundButtons:
   button.led.off()
   print 'led off'
   time.sleep(0.15) #button's LED light will turn off for this amount of time atfer the LED has been turned on

print("button startup done") #if this part of the script was ran correctly "button start up done" will be printed, if not there is an error

while (True):
       time.sleep(1)
       for event in pygame.event.get():
		if event.type == SOUND_END:
			soundButtons [current_sound_button_object].turn_off_led()
			current_sound_button_object = -1
			print('success') #after the button is pressed   

		if pygame.mixer.music.get_busy() == True:
			isPlaying = True
		else:
			if (current_sound_button_object != -1):
				soundButtons[current_sound_button_object].turn_off_led()
				current_sound_button_object = -1

pause()


	
