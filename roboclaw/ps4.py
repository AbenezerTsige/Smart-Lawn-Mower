# ps4Joystick.py
# This code connects the ps4 joystick with the raspberry pi to control the movement of lawn mower and blades.  

############################################
# Library                                  #
############################################
import pygame
import time
import motor
from roboclaw import Roboclaw
import pygame
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

############################################
# Linux comport name                       #
############################################

rc = Roboclaw("/dev/ttyACM0",115200)

###############################################
# Declare Buttons                             #
###############################################

square = 0      # Turn on blades 
ex = 1          # Turn off blades 
circle = 2      # Turn on LED lights 
triangle = 3    # Turn off LED lights

def displayspeed():
    enc1 = rc.ReadEncM1(address)            # Read Motor 1
    enc2 = rc.ReadEncM2(address)            # Read Motor 2
    
    speed1 = rc.ReadSpeedM1(address)        # Speed for Motor 1
    speed2 = rc.ReadSpeedM2(address)        # Speed for Motor 2

    print("Encoder1:")
    if(enc1[0]==1):
        print(enc1[1])
        print(format(enc1[2],'02x'))
    else:
        print("failed")
        
    print("Encoder2:")
    if(enc2[0]==1):
        print(enc2[1])
        print(format(enc2[2],'02x'))
    else:
        print("failed")
        
############################################
# Speed                                    #
############################################

    print("Speed1:")
    if(speed1[0]):
        print(speed1[1])
    else:
        print("failed")
        
    print("Speed2:")
    if(speed2[0]):
        print(speed2[1])
    else:
        print("failed")
        
############################################
# Setup linux usb port communication       #
############################################

rc.Open()
address = 0x80
version = rc.ReadVersion(address)

pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()


# -------- Main Program Loop -----------
while True:
    buttons = 
        
        for event in pygame.event.get():
            
            buttons =  joystick.get_button()
           
            for i in range( buttons ):
        
                if(square == i):
                    GPIO.output(2, GPIO.HIGH)   # Turn on Blades
                          
                elif(ex == i):
                    GPIO.output(3, GPIO.LOW)    # Turn off Blades

                elif(circle == i):
                    GPIO.output(4, GPIO.HIGH)   # Turn on LED

                elif(triangle == i):
                    GPIO.output(10, GPIO.HIGH)  # Turn off LED

            if event.type == pygame.JOYAXISMOTION:
                    
                if( event.axis == 1 ) and (event.value < 0) :
                        North = abs(round(event.value, 2))
                        North = abs(North)
                        print("Up = ", North * 3 )

                        motor.up()
                        time.sleep( North * 1.2 )
                        motor.stop()
                        time.sleep(1)
                        
                elif( event.axis == 1 ) and (event.value == 1) :
                        South = round(event.value, 2)
                        South = abs(South)
                        print("Down = ",South * 1.2 )

                        # motor.down()
                        time.sleep( South * 1.2 )
                        motor.stop()
                        time.sleep(1)
                        
                elif( event.axis == 0 ) and (event.value == 1) :
                        West = round(event.value, 2)
                        West = abs(West)
                        print("Right = ", West * 3)

                       # motor.right()
                        time.sleep( West * 1.2 )
                        motor.stop()
                        time.sleep(1)
                        
                elif( event.axis == 0 ) and (event.value < 0) :
                        East = round(event.value, 2)
                        East = abs(East)
                        print("Left = ", East * 3 )

                       # motor.left()
                        time.sleep( East * 1.2 )
                        motor.stop()
                        time.sleep(1)
                        
                 elif( event.axis == 0 ) and (event.value < 0) :
                        East = round(event.value, 2)
                        East = abs(East)
                        print("Left = ", East * 3 )

                       # motor.left()
                        time.sleep( East * 1.2 )
                        motor.stop()
                        time.sleep(1)
                 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()


        
