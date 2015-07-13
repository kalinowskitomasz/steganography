'''
Author:Daniel Ramirez
TFG: Steganography in TCP/IP protocols
Class:Steganography.py
daniel.ramirezm@e-campus.uab.cat
Development by using scapy a Python Framework
'''

#!/usr/bin/env python
from scapy.all import *

###############################[PATH]#################################
#FILE PATH:'/home/dani/Documents/Final project/python/Steg/steg.txt' 
#if you want send with some payload try with hola as a payload.

class steg(object):

    global tmp,aux,Steg,option,path,t,i,size
    size=10000
    tmp=[]
    #Array for convert from text into integer.
    aux=[]
    Steg=[]
    option='y'
    #Create IP header with Scapy framework
    i=IP()
    #Create TCP header with Scapy framework
    t=TCP()

    def OpenFile(self):
        try:
            #Open the file from directory.
            path = input('Write the path of the file for Steganography:')
            f= open(path, 'r')
            #Ask if you want to add a payload.
            value=input('Do you want add a payload?(y/n):')
            if (option == value):
                payload = input ('Write Payload:')
                t.payload=payload
            while 1:
                c = f.read(1)
                if not c:
                    break
                tmp.append(c)
        except IOError:
            print "Error:Can not open the FILE"
        finally:
            f.close()
        return tmp

    def ConversiontoInteger(self):
        for x in tmp:
            try:
                aux.append(ord(x)*150)
            except:
                print "Error in Type of data"         
        #print len(aux)

        for y in aux:
            if(y>size):
                Steg.append(y)
            else:
                Steg.append(y*8)

        #print len(Steg)
        print "Showing the text Convert to Number:\n"
        print Steg
        return Steg

    def SendingPacket(self):
        #Define some defaults values
        i.version=4
        i.ihl=5
        i.ttl=255
        i.src='127.0.0.1'
        i.dst='127.0.0.1'

        #Source Port
        t.sport=20
        #Destination Port
        t.dport=80
        t.dataofs=5
        t.flags='FS'
        value=input('Do you want send the packet with Steganography:')
        if (option == value):
            for z in range(len(Steg)):
                try:
                    t.window=Steg[z]
                    send(i/t)
                except Exception as e:
                    print e


if __name__ == "__main__":
    try:
        a=steg()
        a.OpenFile()
        a.ConversiontoInteger()
        a.SendingPacket()
    except Exception as e:
        print e
