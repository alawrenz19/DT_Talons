import RPL
RPL.init()
import time 

f_reverse = 1000
neutral = 1500
f_forward = 2000
#anglepersecond = 30

def DT_PWM_Speedrange():
	ServoR = int(raw_input("Pls input what pin you've inserted your right talon into > "))
	RPL.pinMode(ServoR, RPL.PWM)
	ServoL = int(raw_input("Pls input what pin you've inserted your left talon into > "))
	RPL.pinMode(ServoL, RPL.PWM)

	DT_input_R = int(raw_input("Pls input what speed you want to run the right motor at: 4 = Forward_fastest, 3 = Foward_fast, 0 = stop, 2 = Reverse_fast, 1 = Reverse_fastest > "))
	if DT_input_R == 4:
		RPL.pwmWrite(ServoR, 2000, 3000) 
	elif DT_input_R == 3:
		RPL.pwmWrite(ServoR, 1750, 3000) 
	elif DT_input_R == 0:
		RPL.pwmWrite(ServoR, 1500, 3000) 
	elif DT_input_R == 2:
		RPL.pwmWrite(ServoR, 1250, 3000) 
	elif DT_input_R == 1:
		RPL.pwmWrite(ServoR, 1000, 3000) 
	else:
		print("The number you inputted is not an available option. Pls run the code again with one of the 5 numbers.")
	
	DT_input_L = int(raw_input("Pls input what speed you want to run the left motor at: 4 = Forward_fastest, 3 = Foward_fast, 0 = stop, 2 = Reverse_fast, 1 = Reverse_fastest > "))
	if DT_input_L == 4:
		RPL.pwmWrite(ServoL, 2000, 3000) 
	elif DT_input_L == 3:
		RPL.pwmWrite(ServoL, 1750, 3000) 
	elif DT_input_L == 0:
		RPL.pwmWrite(ServoL, 1500, 3000) 
	elif DT_input_L == 2:
		RPL.pwmWrite(ServoL, 1250, 3000) 
	elif DT_input_L == 1:
		RPL.pwmWrite(ServoL, 1000, 3000) 
	else:
		print("The number you inputted is not an available option. Pls run the code again with one of the 5 numbers.")

DT_PWM_Speedrange()

