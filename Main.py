'''
Author:Daniel Ramirez
TFG: Steganography in TCP/IP protocols
Main.py
danielramirezmartin@gmail.com
Development by using scapy a Python Framework
'''

#!/usr/bin/env python
from scapy.all import *
from Steganography import *
from Conversion import *

if __name__ == "__main__":
    try:
        print "########## [Steganography] ##########"
        a=steg()
        a.OpenFile()
        a.ConversiontoInteger()
        a.SendingPacket()
        print "########## [Recovering Message] ##########"
        #Comentar codigo
        b=Conversion()
        b.converter()
    except Exception as e:
        print e
