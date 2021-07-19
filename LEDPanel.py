from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

COLORS = {'red': [255,0,0],
          'green': [0,255,0],
          'blue,': [0,0,255],
          'yellow': [255, 255, 0]}

class LEDPanel():
    def __init__(self):
        self.uhm = UnicornHATMini();
        
        self.hat_width, self.hat_height = self.uhm.get_shape()
        
        self.uhm.set_brightness(0.1)
        self.uhm.set_rotation(0)


    def setColor(self, color):
        if color in COLORS:
            self.uhm.set_all(COLORS[color])
        else:
            self.uhm.set_all(*color)
        self.uhm.show()

    def setImage(self, imagePath):
        image = Image.open(imagePath)
        self.uhm.set_image(image)
        self.uhm.show()

    def scrollText(self, text):
        #https://github.com/pimoroni/unicornhatmini-python/blob/master/examples/text.py
        pass

    def clear(self):
        self.uhm.clear()