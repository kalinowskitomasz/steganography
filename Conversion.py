'''
Author:Daniel Ramirez
TFG: Steganography in TCP/IP protocols
daniel.ramirezm@e-campus.uab.cat
Development by using scapy a Python Framework
'''

#!/usr/bin/env python
#FILE PATH:'/home/dani/Documents/Final project/python/Steg/try2.txt'---> with payload
#FILE PATH:'/home/dani/Documents/Final project/python/Steg/packets.txt'---> withput payload

class Conversion(object):
	
	global tmp,aux,opt,Decrypt,Text,Original,path,option
	tmp=[]
	aux=[]
	opt=[]
	Decrypt=[]
	Text=[]
	Original=[]
	option='y'

	def converter(self):
		#Open the file with all the packet send.
		path=input('Insert the path of the packets for analyze: ')
		f1= open(path, 'r')
		fo=f1.readlines()[::2]
		answer=input("The Packet have payload?:")
		if(answer!=option):
			#Remove all characters and new lines,empty line  and select the field where are the steganography, in this case is:TCP window.
			for t in fo:
				t=t.replace('-','').replace('+','').replace('\n','').replace('|','')
				tmp.append('0x'+t[100:-9])
				aux=tmp[1::2]
		else:
			for t in fo:
				t=t.replace('-','').replace('+','').replace('\n','').replace('|','')
				tmp.append('0x'+t[100:-19])
				aux=tmp[1::2]

		#Convert all the hexadecimal number into an integer and store in opt array.
		for w in range(len(aux)):
			opt.append(int(aux[w],16))
		print opt

		#Using the inverse operation for having the correct number.
		for u in opt:
			Decrypt.append((u)/150)
		for x in Decrypt:
		    if(x < 256 ):
		    	Text.append(x)
		    else:
		        Text.append(x/8)
		#Convert all the numbers into characters.
		for w in Text:
		    Original.append(chr(w))

		print Original[:-1]

		namefile=input("Write the output file name: ")
		print "Writing into the file..."

		#Write the message into a file txt.
		f2=open('/home/dani/Documents/Final project/python/Steg/'+namefile,'w')
		for z in Original[:-1]:
			f2.write(z)

		f2.close()

		f1.close()

		print "Closing files..."

if __name__ == "__main__":
	b=Conversion()
	b.converter()