########################################################################################################
# Class Declarations                                                                                   #              
########################################################################################################
#import motor     # Includes all the manuever fucntions  
from numcrunch import crunch            # Calculates distance(Imd,Lbd,Rbd, zlb and zrb)
from marvelmind import MarvelmindHedge  # Marvelmind class, claculates Left and Right Beacon values

import time
from time import sleep
import sys
import RPi.GPIO as GPIO
import math

####################################################################
# Pi GPIO Initalize                                                #              
####################################################################    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

####################################################################
# Import Distance Calculations  and Motor Control functions        #              
####################################################################

# call numcrunch.py file 
robo = motor() # call motor.py file 

####################################################################
# SCABY Route Pattern Option: 1                                    #              
####################################################################   
# Start Horizontal Mow
def HorzMow():
    motor.up()
    time.sleep(4) 
    motor.stop()

    motor.right()
    time.sleep(4) 
    motor.stop()

    motor.left()
    time.sleep(4) 
    motor.stop()

    motor.down()
    time.sleep(4) 
    motor.stop()

####################################################################
# SCABY Route Pattern Option: 2                                    #              
####################################################################   
# Start Vertical Mow
def VertMow():
    motor.up()
    time.sleep(4) 
    motor.stop()

    motor.right()
    time.sleep(4) 
    motor.stop()

    motor.left()
    time.sleep(4) 
    motor.stop()

    motor.down()
    time.sleep(4) 

####################################################################
# SCABY Route Pattern Option: 1                                    #              
####################################################################
def SDbot():
    print("===================================================")
    print("                   SCABY")
    print("===================================================")
    print("\nThank you for choosing SCABY!")
    print("For a Horzontal mow Please enter 1 ")
    mrout = input("For a Vertical mow Please enter 2\n")

    if(mrout == 1):
         print("You have chosen Horzontal mow")
         HorzMow()
    
    elif(mrout == 2):
         print("You have chosen Vertical mow")
         VertMow()

    return mrout
 

####################################################################
# Main                                                             #              
####################################################################    

SDbot()  

GPIO.cleanup() # Cleans up used ports
