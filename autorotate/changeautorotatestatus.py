#!/usr/bin/env python
import os
from gi.repository import Notify

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

status = readFile('/home/marc/.scripts/status.txt')
if status[0] == "on":
    writeFile('/home/marc/.scripts/status.txt', ["off"])
    Notify.init ("Rotation-ON")
    RotationOFF=Notify.Notification.new ("Rotation","Screenrotation is now turned OFF","dialog-information")
    RotationOFF.show ()
if status[0] == "off":
    writeFile('/home/marc/.scripts/status.txt', ["on"])
    Notify.init ("Rotation-OFF")
    RotationON=Notify.Notification.new ("Rotation","Screenrotation is now turned ON","dialog-information")
    RotationON.show ()
