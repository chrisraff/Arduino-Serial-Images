import psutil
import serial
import serial.tools.list_ports
import sys
from time import sleep, time
from numpy import sin
from tqdm import tqdm

baudrate = 115200

device = None

if len(sys.argv) >= 2:
    device = sys.argv[1]
else:
    # connect to the first com port in the list
    comlist = serial.tools.list_ports.comports()
    print(f'Available ports: {[c.device for c in comlist]}\nAttempting to connect to {comlist[0]}...')
    device = comlist[0].device

ser = serial.Serial(device, baudrate, timeout = 1)

print(f'connected to {ser.name}')

disp = tqdm()

while True:
    data = b'[.' # start the frame, specify 64 pixels of data
    for i in range(64): # for each pixel
        data += bytes( [int( 127*sin(2*time()) + 127), 5, i*2] ) # the rgb values for this pixel

        # the serial buffer can only hold 256 bytes at a time on ESP32
        # if the image is really large, it may be necessary to send parts at a time
        # but probably not since the arduino usually processes the data quicker than it is written
        # if i % 21 == 0 or False:
        #     ser.write(data)
        #     data = b''
        #     sleep(0.008)
    data += b']' # end the frame (arduino updates the display)

    # print(''.join([str(chr(c)) for c in data])) # print the string we sent

    ser.write(data)

    disp.update()
