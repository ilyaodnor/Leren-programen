import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from expert import challenges
robotArm = RobotArm(challenges[5],1)
aantaal =0
r = 0
b = 0
g = 0
klueren = {
    'red': 0,
    'yellow':0,
    'blue':0
}
robotArm.moveRight()
while robotArm.stackIndex() <10:
    robotArm.grab()
    klueren[robotArm.scan()]+=1
    robotArm.drop()
    if robotArm.stackIndex()!=9:
        robotArm.moveRight()
    elif robotArm.stackIndex() == 9:
        break
    print(klueren)

while robotArm.stackIndex()!=0:
    aantaal=0

    if r>b and r> g:
        robotArm.grab()
        if robotArm.scan() == 'red':
            while robotArm.stackIndex()!=0:
                robotArm.moveLeft()
                aantaal +=1
            robotArm.drop()
            for i in range(aantaal-1): robotArm.moveRight()
        elif robotArm.scan() == 'yellow' or 'blue':
            robotArm.drop()
            robotArm.moveLeft()
    elif g>b and g>r:
        robotArm.grab()
        if robotArm.scan() == 'yellow':
            while robotArm.stackIndex()!=0:
                robotArm.moveLeft()
                aantaal +=1
            robotArm.drop()
            for i in range(aantaal-1): robotArm.moveRight()
        elif robotArm.scan() == 'red' or 'blue':
            robotArm.drop()
            robotArm.moveLeft()
    elif b>g and b>r:
            robotArm.grab()
            if robotArm.scan() == 'blue':
                while robotArm.stackIndex()!=0:
                    robotArm.moveLeft()
                    aantaal +=1
                robotArm.drop()
                for i in range(aantaal-1): robotArm.moveRight()
            elif robotArm.scan() == 'red' or 'yellow':
                robotArm.drop()
                robotArm.moveLeft()
robotArm.report()
