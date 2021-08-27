from threading import Thread, Lock
from time import sleep

class DeviceCodePrinter():
    def __init__(self, device_user_code):
        self.code = device_user_code
        self.m = Lock()

    # Some concerning uses to explore calling this multiple times without a complete
    def printUntilComplete(self, printFnc=print, delay=30):
        self.m.acquire()
        self.incomplete = True
        self.m.release()

        print_thread = Thread(target=self.doUntilComplete, args=(printFnc, delay, self.code), daemon=True)
        print_thread.start()

    # Really don't wanna call this directly
    def doUntilComplete(self, fnc, loop_delay, *args):
        while self.incomplete: #Just reading don't care about lock
            fnc(*args)
            sleep(loop_delay)

    def complete(self):
        self.m.acquire()
        self.incomplete = False
        self.m.release()
            
            