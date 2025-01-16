import gpiozero as gp
from time import sleep



# Set up the GPIO pin
stepper = gp.LED(17)

while True:
    stepper.on()
    sleep(0.01)
    stepper.off()
    sleep(0.01)