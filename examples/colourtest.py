import pixelzero
import time

pixelno = 8
n = pixelzero.NeoPixel(18, pixelno)

while True:
    for r in range(pixelno):
        n[r] = (255,0,0)
        n.show()

    time.sleep(1)
    
    for g in range(pixelno):
        n[g] = (0,255,0)
         n.show()

    time.sleep(1)
    
    for b in range(pixelno):
        n[b] = (0,0,255)
        n.show()
    
    time.sleep(1)
