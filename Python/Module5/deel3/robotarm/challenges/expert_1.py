import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from expert import challenges
robotArm = RobotArm(challenges[1],2)
aantaal = 1
for i in range(4):
        for j in range(aantaal):
            robotArm.grab()
            for k in range(5): robotArm.moveRight()
            robotArm.drop()
            if j !=aantaal-1:
                  for k in range(5):
                        robotArm.moveLeft()
            else:
                  for k in range(4):
                        robotArm.moveLeft()
        if i == 4:
              break
        else:
              aantaal+=1
robotArm.report()