![alt text](pixelzerologo.png)
# Welcome to the PixelZero repository!

# About
PixelZero is a zero boilerplate neopixel control library for the Raspberry Pi. We've ported the MicroPython neopixel library to the Raspberry Pi to make neopixels much easier to use in Python, you can get started with just a few lines of code. Here is an example using 8 neopixels on BCM pin 18 turning pixel 5 red:

```python
from pixelzero import *

np = NeoPixel(18, 8)

np[5] = (255, 0, 0)
np.show()
```


# Installing

PixelZero can be downloaded to your Raspberry Pi via PyPi. This will install the library so you can use it with Python 3. We are also working on a one line installer that will install the library and expamples, but this is not ready yet. To install, fire up Terminal which you'll find in Menu > Accessories > Terminal on your Raspberry Pi desktop, which is shown below:

![alt text](https://github.com/AllAboutCode/EduBlocks/blob/tarball-install/misc/step1new.png)

In the terminal window you have just opened, type the command below to install the library (if you get any errors, check for spelling mistakes):

```bash
sudo pip3 install pixel-zero
```

# Contributing:

If you want to contribute, you should first clone this repository, `cd` to the library directory on your Raspberry Pi, and then  run:

```bash
sudo python3 setup.py install
```
