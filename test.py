import time
from leds import send_leds

controller = '10.77.84.158'
port = 6454
universe = 0
num_leds = 170
delay = 0.05

# Red background
leds = [(255,0,0) for _ in range(num_leds)]

for i in range(num_leds):
    # Set to white
    leds[i] = (255,255,255)
    send_leds(controller, port, universe, leds)

    # Wait a bit
    time.sleep(0.05)

    # Back to red
    leds[i] = (255, 0, 0)



