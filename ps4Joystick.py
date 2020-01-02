import pygame
import time
import motor

pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

# main loop
while True:
        
        for event in pygame.event.get():

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
                
pygame.quit ()

        
