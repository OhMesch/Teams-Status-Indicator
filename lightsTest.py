import time
import json
import msal
import requests
from LEDPanel import LEDPanel

a = LEDPanel()
a.setColor('red')
time.sleep(5)
a.setColor('yellow')
time.sleep(5)
a.setColor('blue')
time.sleep(5)
a.setColor('green')
time.sleep(5)