import gpiozero
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(24)

def pressed(self):
               print "pressed"

button.when_pressed = led.on
button.when_pressed = pressed
button.when_released = led.off 

pause()




