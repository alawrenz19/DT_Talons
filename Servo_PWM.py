import RPL
RPL.init()
import time 

f_reverse = 1000
neutral = 1500
f_forward = 2000
#anglepersecond = 30

def DT_PWM_Establish():
	TalonR = int(raw_input("Pls input what pin \
	you've inserted your right talon into >")
	RPL.pinMode(ServoR, RPL.PWM)
	TalonL = int(raw_input("Pls input what pin \
	you've inserted your left talon into >")
	RPL.pinMode(ServoL, RPL.PWM)

def DT_Speed():
	DT_input = int(raw_input("Pls input what speed you want to run the motors at: 4 = Forward_fastest, \
	3 = Foward_fast, 0 = stop, 2 = Reverse_fast, 1 = Reverse_fastest > "))
	if DT_input = 4:
		RPL.pwmWrite(0, 2000, 3000) 
	if DT_input = 3:
		RPL.pwmWrite(0, 1750, 3000) 
	if DT_input = 0:
		RPL.pwmWrite(0, 1500, 3000) 
	if DT_input = 2:
		RPL.pwmWrite(0, 1250, 3000) 
	if DT_input = 1:
		RPL.pwmWrite(0, 1000, 3000) 
	else: print("The number you inputted is not an available option. Pls run the code again with one of the 5 numbers.")

DT_PWM_Establish()
DT_Speed()
