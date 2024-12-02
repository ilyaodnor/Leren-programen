import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from basic import challenges
robotArm = RobotArm(challenges[5],3)
robotArm.moveRight()
robotArm.grab()
robotArm.scan()
if robotArm.scan() == 'red': 
    robotArm.moveLeft()
    robotArm.drop()
elif robotArm.scan()== 'yellow':
    robotArm.moveRight()
    robotArm.drop()
robotArm.report()
robotArm.help()