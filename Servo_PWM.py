import RPL
RPL.init()
import time 

f_reverse = 1000
neutral = 1500
f_forward = 2000
# anglepersecond = 

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
    if time.time() > currenttime + T:
      RPL.pwmWrite(0, 1500, 3000)
  if degreeturn < 90:
    TT = degreeturn / anglepersecond
    while time.time() < currenttime + TT:
      RPL.pwmWrite(0, 1000, 3000)
    if time.time() > currenttime + T:
      RPL.pwmWrite(0, 1500, 3000)
    
turn()



