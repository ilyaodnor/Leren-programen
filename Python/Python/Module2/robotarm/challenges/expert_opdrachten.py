import sys
sys.path.insert(0,'/Users/ilya/Documents/GitHub/School/Softwere dev./python/Leren-programen/Python/Module2/robotarm')
from RobotArm import RobotArm
from expert import challenges
robotArm = RobotArm(challenges[5],2)
kleuren = {'red': 0,'yellow':0,'blue':0}
robotArm.moveRight()
while robotArm.stackIndex() <10:
    robotArm.grab()
    kleuren[robotArm.scan()]+=1
    robotArm.drop()
    if robotArm.stackIndex()!=9:
        robotArm.moveRight()
    elif robotArm.stackIndex() == 9:
        break
    print(kleuren)
max = 0
max_color=''
for i in kleuren:
    if kleuren[i]>max:
        max=kleuren[i]
        max_color = i
print(max_color)
while robotArm.stackIndex()!=0:
    aantaal=0
    robotArm.grab()
    if robotArm.scan() == max_color:
        print(max)
        while robotArm.stackIndex()!=0:
            robotArm.moveLeft()
            aantaal +=1
        robotArm.drop()
        for i in range(aantaal-1): robotArm.moveRight()
    else:    
        print(max)
        robotArm.drop()
        robotArm.moveLeft()  
robotArm.report()
