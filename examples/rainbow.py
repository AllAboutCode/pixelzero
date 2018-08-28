# Original example by Gadgetoid from Pimoroni. Reference: https://github.com/pimoroni/unicorn-hat/blob/master/examples/rainbow.py

import math
import time
import pixelzero

pixels = 8

np = pixelzero.NeoPixel(18, pixels)

i = 0.0
offset = 30
while True:
        i = i + 0.3
        
        for x in range(pixels):
                r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                r = max(0, min(255, r + offset))
                g = max(0, min(255, g + offset))
                b = max(0, min(255, b + offset))
                np[x] = (int(r),int(g),int(b))
        np.show()
time.sleep(0.01)
