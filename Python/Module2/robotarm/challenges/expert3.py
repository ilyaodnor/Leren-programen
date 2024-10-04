import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from expert import challenges
robotArm = RobotArm(challenges[3],2)
aantaal =1
while robotArm.stackEmpty() == False:
    robotArm.grab()
    for i in range(aantaal):robotArm.moveRight()
    robotArm.drop()
    for i in range(aantaal):robotArm.moveLeft() 
    aantaal+=1
robotArm.showSolution()
robotArm.report()