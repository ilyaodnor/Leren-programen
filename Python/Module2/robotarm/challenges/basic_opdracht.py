import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from basic import challenges
robotArm = RobotArm(challenges[4],3)
robotArm.grab()
for i in range(9): robotArm.moveRight()
robotArm.drop()
for i in range(5): robotArm.moveLeft()
robotArm.grab()
for i in range(5): robotArm.moveRight()
robotArm.drop()
for i in range(2): robotArm.moveLeft()
robotArm.grab()
for i in range (2): robotArm.moveRight()
robotArm.drop()
robotArm.report()
