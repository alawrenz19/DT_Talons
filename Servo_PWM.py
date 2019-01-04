import RPL
RPL.init()
import time 

f_reverse = 1000
neutral = 1500
f_forward = 2000
#anglepersecond = 30

ServoR = int(raw_input("S_R > "))
ServoL = int(raw_input("S_L > "))

RPL.pinMode(ServoR, RPL.PWM)
RPL.pinMode(ServoL, RPL.PWM)

def turn():
  degreeturn = int(raw_input("Deg_T > "))
  currenttime = time.time()
  if degreeturn > 90:
    TT = (degreeturn - 90) / anglepersecond
    while time.time() < currenttime + TT:
      RPL.pwmWrite(0, 2000, 3000) 
    if time.time() > currenttime + TT:
      RPL.pwmWrite(0, 1500, 3000)
  if degreeturn < 90:
    TT = degreeturn / anglepersecond
    while time.time() < currenttime + TT:
      RPL.pwmWrite(0, 1000, 3000)
    if time.time() > currenttime + TT:
      RPL.pwmWrite(0, 1500, 3000)
    
def drive(x2,y2): 
  v = vector(x2, y2) 
  length = v.mag()
  return length
  abslength = abs(magnitude) * 15.24
  Runtime = Length / 13.3
  currenttime = time.time()
 	while time.time() < (currenttime + Runtime):
    		RPL.servoWrite(motorL, 2000)
		RPL.servoWrite(motorR, 1000)
  	if time.time() > (currenttime + Runtime):
    		RPL.servoWrite(motorL, 0)
    		RPL.servoWrite(motorR, 0)



