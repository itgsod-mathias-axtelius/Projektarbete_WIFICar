#!/usr/bin/env python
#
#Classic controller sticks:
# R stick: greater than or equil to 25 to go forward, less than or equil to 7 to go backward, 17 is at rest.
# L stick: greater than or equil to 53 to go forward, less than or equil to 12 to go backward, 32 is at rest.   
import socket
import cwiid
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Press button 1 + 2 on your Wii Remote...'
wm=cwiid.Wiimote()
print 'Wii Remote connected...'
time.sleep(1)
Rumble = False
wm.rpt_mode = cwiid.RPT_CLASSIC
while True:
 ip = raw_input("IP ADDRESS OF ROBOT >>>")
 client.connect((ip, 6000)) 
 print "Connected to ", ip
 print "READY!"
 while True:
  right = wm.state['classic']['r_stick'][1]
  left = wm.state['classic']['l_stick'][1]
  if (right > 24):
   bit1 = 2
  elif (right < 8):
   bit1 = 0
  else:
   bit1 = 1
  if (left > 52):
   bit2 = 2
  elif (left < 13):
   bit2 = 0
  else:
   bit2 = 1
  data = "%s%s" % (int(bit1), int(bit2)) 
  rts = client.recv(1)
  if (rts == '*'):
   client.send(data)
   bit1 = 0
   bit2 = 0
  else:
   pass
  
