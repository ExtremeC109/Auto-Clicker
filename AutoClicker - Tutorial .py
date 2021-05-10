import win32api, win32con, threading, time

VK_CODE = {
    "alt": 0x12,          #alt
    "tab": 0x09,          #tab
    "startPause": 0x46,   #f
    "quit": 0x23,         #end
    "smartDelay": 0x4F,   #o
    "switchButton": 0x52  #r
}


class Mouse(threading.Thread):

    def __init__(self):
        super(Mouse, self).__init__()
        self.running = True
        self.autoClickerOn = False
        self.button = True 
        self.delay = float(input("Delay Time: "))
    
    def quit(self):
        self.running = False

    def run(self):
        while self.running:
            while self.autoClickerOn:
                if self.button:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0 , 0)
                    time.sleep(self.delay)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0 , 0)
                else:
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0 , 0)
                    time.sleep(self.delay)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0 , 0)
    
    def switchButton(self):
        if self.button:
            self.button = False
        else:
            self.button = True
    
    def autoClickerSwitch(self):
        if self.autoClickerOn:
            self.autoClickerOn = False
        else:
            self.autoClickerOn = True

mouseThread = Mouse()
mouseThread.start()

while True:
    if win32api.GetKeyState(VK_CODE["startPause"]) < 0:
        mouseThread.autoClickerSwitch()
        time.sleep(0.2)
    if win32api.GetKeyState(VK_CODE["switchButton"]) < 0:
        mouseThread.switchButton()
        time.sleep(0.2)
    if win32api.GetKeyState(VK_CODE["alt"]) < 0 and win32api.GetKeyState(VK_CODE["tab"]) < 0:
        if mouseThread.autoClickerOn:
            mouseThread.autoClickerSwitch()
            time.sleep(0.2)
    if win32api.GetKeyState(VK_CODE["quit"]) < 0:
        mouseThread.quit()
        break