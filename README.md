Surface3-Scripts
================

Some simple scripts for Linux on the Surface Pro 3.

Autorotate: autorotate.py run with python2 needs 

autorotate.py
=============

Script for managing autorotation of the screen and deactivation of the touchscreen through the pen.

Instalation
-----------
* install libnotify and python2-gobject (needed for notifications)
* copy autorotate.py, touch.py, changeautorotatestatus.py, touch.txt, status.txt in the same folder
  
Usage
-----
Start script:
```
$ python2 /path/to/autorotate.py
```
Deactivate/reactivate autorotation:
```
$ python2 /path/to/changeautorotatestatus.py
```
Deactivate/reactivate touch:
```
$ python2 path/to/touch.py
```
