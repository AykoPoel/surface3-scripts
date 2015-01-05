#!/usr/bin/env python2
import os

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


devicename = "NTRG0001:01 1B96:1B05"
penname = "'NTRG0001:01 1B96:1B05 Pen'"
path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

status = readFile(os.path.join(path, 'touch.txt'))
if str(status[0]) == "on":
    writeFile(os.path.join(path, 'touch.txt'), ["off"])
if str(status[0]) == "off":
    writeFile(os.path.join(path, 'touch.txt'), ["on"])
