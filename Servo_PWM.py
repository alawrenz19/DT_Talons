from src/bsmLib import RPL
RPL.init()

f_reverse = 1000
neutral = 1500
f_forward = 2000

ServoR = int(raw_input("S_R > "))
ServoL = int(raw_input("S_L > "))

RPL.pinMode(ServoR, RPL.PWM)
RPL.pinMode(ServoL, RPL.PWM)







