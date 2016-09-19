from adxl345 import ADXL345
import time
import math
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#TODO Change the hard coded addr to a function that will find the server
server_address =('169.254.210.109',1234) #Enter your IP of ethernet connection not Pi's IP
sock.connect(server_address)


rollpitch = ""

adxl345 = ADXL345()

while True:    
    axes = adxl345.getAxes(True)
    x = axes['x']
    y = axes['y']
    z = axes['z']
    #calculation of tilt
    roll = y/(math.sqrt(z*z + x*x))
    rolldeg = math.atan(roll)*(180/(math.pi))
    rolldeg = round(rolldeg,2)
    pitch = x/(math.sqrt(z*z + y*y))
    pitchdeg = math.atan(pitch)*(180/(math.pi))
    pitchdeg = round(pitchdeg,2)

    rollpitch = str(rolldeg) + " " + str(pitchdeg)
    print rollpitch
    sock.sendto(rollpitch,server_address)
    
    time.sleep(0.01)
