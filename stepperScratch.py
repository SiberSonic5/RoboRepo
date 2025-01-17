import gpiozero as gp
from time import sleep


# Set up a list of devices to close at end
devices = []

# Set up the GPIO pin
stepper = gp.LED(17)
devices.append(stepper)


try:
    while True:
        stepper.on()
        sleep(0.0006)
        stepper.off()
        sleep(0.0006)
except KeyboardInterrupt:
    print("Cleaning up GPIO")
finally: 
    for device in devices:
        device.close()
