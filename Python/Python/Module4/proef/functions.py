import time , math
from termcolor import colored
from data import *

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount*25

def getPersonCashInGold(personCash:dict) -> float:
    return copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + platinum2gold(personCash['platinum'])+ personCash['gold']

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    return copper2gold(JOURNEY_IN_DAYS*((COST_FOOD_HUMAN_COPPER_PER_DAY*people) +(COST_FOOD_HORSE_COPPER_PER_DAY* horses) ))

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item.get(key) == value]

def getAdventuringPeople(people:list) -> list:
    lijst = []
    for i in people:
        if i['adventuring'] == True:
            lijst.append(i)
    return lijst 

def getShareWithFriends(friends:list) -> list:
    lijst = []
    for i in friends:
        if i['shareWith'] == True:
            lijst.append(i)
    return lijst 

def getAdventuringFriends(friends:list) -> list:
    lijst = []
    for i in friends:
        if i['shareWith'] == True and i['adventuring'] == True:
            lijst.append(i)
    return lijst 

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    if people%2 == 0:
        return people//2
    elif people%2 != 0:
        return people//2+1


def getNumberOfTentsNeeded(people:int) -> int:
    if people %3 == 0:
        return people//3
    elif people%3 ==1 or people%3 == 2:
        return people//3 +1

def getTotalRentalCost(horses:int, tents:int) -> float:
    cost_per_tent_per_day = tents *(COST_TENT_GOLD_PER_WEEK) * math.ceil(JOURNEY_IN_DAYS/7)
    cost_per_horse_per_day_in_gold = horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    
    total_cost =  cost_per_horse_per_day_in_gold + cost_per_tent_per_day
    return total_cost
##################### O08 #####################

def getItemsAsText(items: list) -> str:
    lijst = []
    for i in items:
        
        lijst.append(f"{i['amount']}{i['unit']} {i['name']}")

    if len(lijst) > 1:
        return ", ".join(lijst[:-1]) + " & " + lijst[-1]
    elif lijst:
        return ''.join(lijst)
    else:
        return ""
def getItemsValueInGold(items:list) -> float:
    cost = []
    for i in items:
        if i['price']['type'] == 'platinum':
            cost.append(platinum2gold(i['price']['amount'])*i['amount'])
        elif i['price']['type'] == 'gold':
            a =float(i['price']['amount'])*i['amount']/1
            cost.append(a)
        elif i['price']['type'] == 'silver':
            cost.append(silver2gold(i['price']['amount'])*i['amount'])
        elif i['price']['type'] == 'copper':
            cost.append(copper2gold(i['price']['amount'])*i['amount'])
    return round(sum(cost),2)

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()