#!/usr/bin/env python2
import time
import os

#FUNCTIONS
def readFile(path): #self.filename
    myDatei = open(path, "r")
    myList = []
    #Liste aus Datei erstellen
    for Line in myDatei:
        Line = Line.rstrip()
        #Line = Line.decode('utf8')
        myList.append(Line)
    myDatei.close()
    return(myList)

def writeFile(path, myList): #self.filename
    myDatei = open(path, "w")
    #Liste aus Datei erstelle
    myDatei.writelines(myList)
    myDatei.close()

def refreshtouch():
    os.system('xinput disable "NTRG0001:01 1B96:1B05"')
    os.system('xinput enable "NTRG0001:01 1B96:1B05"')

#PARAMETERS
count = 0
path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
print (path)

devicename = "'NTRG0001:01 1B96:1B05'"
penname = "'NTRG0001:01 1B96:1B05 Pen'"
freq = 10.0  # frequency to read the accelerometer

# Look for accelerometer
while count <= 9:
    if os.path.exists('/sys/bus/iio/devices/iio:device' + str(count) + '/in_accel_scale') == True:
        dpath = '/sys/bus/iio/devices/iio:device0/' # directory of accelerometer device (iio)
        break
    count = count + 1
#print(dpath)

#Commands for correct rotation
normal = 'xrandr -o normal; '+'xinput set-prop ' + devicename +" 'Coordinate Transformation Matrix' 1 0 0 0 1 0 0 0 1;"+'xinput set-prop ' + penname +" 'Coordinate Transformation Matrix' 1 0 0 0 1 0 0 0 1;"
inverted = 'xrandr -o inverted; '+'xinput set-prop ' + devicename +" 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1;"+'xinput set-prop ' + penname +" 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1;"
right = 'xrandr -o left; '+'xinput set-prop ' + devicename +" 'Coordinate Transformation Matrix' 0 -1 1 1 0 0 0 0 1;"+'xinput set-prop ' + penname +" 'Coordinate Transformation Matrix' 0 -1 1 1 0 0 0 0 1;"
left = 'xrandr -o right; '+'xinput set-prop ' + devicename +" 'Coordinate Transformation Matrix' 0 1 0 -1 0 1 0 0 1;"+'xinput set-prop ' + penname +" 'Coordinate Transformation Matrix' 0 1 0 -1 0 1 0 0 1;"

current_state = 0 # 0 normal, 1 inverted, 2 right, 3 left
with open(dpath + 'in_accel_scale') as f:
    scale = float(f.readline())
while True:
    previous_state = current_state
    status = readFile(os.path.join(path, 'status.txt'))
    print(status)
    if str(status[0]) == "on":
        with open(dpath + 'in_accel_x_raw', 'r') as fx:
            with open(dpath + 'in_accel_y_raw', 'r') as fy:
                with open(dpath + 'in_accel_z_raw', 'r') as fz:
                    time.sleep(1.0/freq)
                    thex = float(fx.readline())
                    they = float(fy.readline())
                    thez = float(fz.readline())
                    print("x:" + str(thex))
                    print("y:" + str(they))
                    print("z:" + str(thez))
                    if (thex >= 65000 or thex <=650):
                        if (they <= 65000 and they >= 64000):
                            print("normal!")
                            os.system(normal)
                            current_state = 0
                        if (they >= 650 and they <= 1100):
                            print("inverted!")
                            os.system(inverted)
                            current_state = 1
                    if (thex <= 64999 and thex >= 650):
                        if (thex >= 800 and thex <= 1000):
                            print ("right!")
                            os.system(right)
                            current_state = 2
                        if (thex >= 64500 and thex <=64700):
                            print ("left!")
                            os.system(left)
                            current_state = 3
    if str(status[0]) == "off":
        time.sleep(1.0)
    if current_state != previous_state:
        refreshtouch()
        print "Touchscreen refreshed"
