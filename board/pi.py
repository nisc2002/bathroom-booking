import RPi.GPIO as gpio

gpio.setwarnings(False) # Ignore warning for now
gpio.setmode(gpio.BCM)

# blue button: gpio5
# red button: gpio6

gpio.setup(5, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(6, gpio.IN, pull_up_down=gpio.PUD_UP)

def bluePressed(channel):
    print("blue pressed")

def redPressed(channel):
    print("red pressed")

gpio.add_event_detect(5, gpio.FALLING, callback=bluePressed)
gpio.add_event_detect(6, gpio.FALLING, callback=redPressed)

message = input("Press enter to quit \n\n")
gpio.cleanup()


# try:
#     while True:
        
# except KeyboardInterrupt:
#     gpio.cleanup()