import socket #import libraries
import time # import libraries
import RPi.GPIO as GPIO # import libraries
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
array = []
rts = '*'
bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a server object called 'bot'
port = 6000 #port number for the socket. 5000 to 8000 work for me
bot.bind(('', int(port))) #bind the server object called bot to the pi's current ip address and port 6000
bot.listen(5) #listen for up to five connections
client, address = bot.accept() #accept a connection
while True:
 client.send(rts)
 data = client.recv(2)
 for char in data:
  array.append(char)
 if (int(array[0]) == 2):
  GPIO.output(21, False)
  GPIO.output(4, True)
 elif (int(array[0]) == 0):
  GPIO.output(4, False)
  GPIO.output(21, True)
  else:
   GPIO.output(21, False)
   GPIO.output(4, False)
 if (int(array[1]) == 2):
  GPIO.output(18, False)
  GPIO.output(21, True)
 elif (int(array[1]) == 0):
  GPIO.output(21, False)
  GPIO.output(18, True)
  else:
   GPIO.output(18, False)
   GPIO.output(21, False)
 array = []  
  
 
