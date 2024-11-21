import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from master import challenges
robotArm = RobotArm(challenges[4],2)
kleuren_lijst = []
dictionary = {}
for i in range(4):
    robotArm.grab()
    robotArm.moveRight()
    kleuren_lijst.append(robotArm.scan())
    robotArm.drop()
    robotArm.moveLeft()
while robotArm.stackIndex()!= 6: robotArm.moveRight()
getal = 0
for i in range(4):
    for j in range(8):
        if robotArm.stackEmpty() == True or  robotArm.stackIndex()<=1:
            robotArm.moveRight()
        elif robotArm.stackEmpty() == False and robotArm.stackIndex()>1:    
            robotArm.grab()
            if robotArm.scan()== kleuren_lijst[getal]:
                getal+=1
                while robotArm.stackIndex()!= 0: robotArm.moveLeft()
                robotArm.drop()
                continue
            else:
                robotArm.drop()
                if robotArm!= 9:
                    robotArm.moveRight()

                
            
    

robotArm.report()