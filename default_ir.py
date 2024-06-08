import time
import serial # type: ignore

class Command:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code

def Send(command):
    ser.write(bytes(command, 'utf-8'))
    time.sleep(0.5)

usbport = 'COM8'
ser = serial.Serial(usbport, 9600, timeout=0.1)
time.sleep(2)