#!/usr/bin/env python2
import os
from gi.repository import Notify

path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

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

status = readFile(os.path.join(path, 'status.txt'))
if status[0] == "on":
    writeFile(os.path.join(path, 'status.txt'), ["off"])
    Notify.init ("Rotation-ON")
    RotationOFF=Notify.Notification.new ("Rotation","Screenrotation is now turned OFF","dialog-information")
    RotationOFF.show ()
if status[0] == "off":
    writeFile(os.path.join(path, 'status.txt'), ["on"])
    Notify.init ("Rotation-OFF")
    RotationON=Notify.Notification.new ("Rotation","Screenrotation is now turned ON","dialog-information")
    RotationON.show ()
