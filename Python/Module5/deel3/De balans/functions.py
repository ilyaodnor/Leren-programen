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
    if copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + platinum2gold(personCash['platinum'])+ personCash['gold'] == 0:
        return 0.0

    return copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + platinum2gold(personCash['platinum'])+ personCash['gold']

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    return copper2gold(JOURNEY_IN_DAYS*((COST_FOOD_HUMAN_COPPER_PER_DAY*people) +(COST_FOOD_HORSE_COPPER_PER_DAY* horses) ))

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item.get(key) == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True) 

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True) 
def getAdventuringFriends(friends: list) -> list:
    adventuring_friends = getAdventuringPeople(friends)
    sharing_friends = getShareWithFriends(friends)
    return [friend for friend in adventuring_friends if friend in sharing_friends]







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
            cost.append(i['price']['amount']*i['amount'])
        elif i['price']['type'] == 'silver':
            cost.append(silver2gold(i['price']['amount'])*i['amount'])
        elif i['price']['type'] == 'copper':
            cost.append(copper2gold(i['price']['amount'])*i['amount'])
    return float(round(sum(cost),2))

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    lijst = []
    for i in people:
        lijst.append(platinum2gold(i['cash']['platinum'])+i['cash']['gold']+silver2gold(i['cash']['silver'])+copper2gold(i['cash']['copper']))
    return float(sum(lijst))
##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
        lijst = []
        for i in investors:
            if i['profitReturn']<10:
                lijst.append(i)
        return lijst
def getAdventuringInvestors(investors:list) -> list:
    lijst = getInterestingInvestors(investors)
    lijst2 =[]
    for i in lijst:
        if i['adventuring'] == True:
            lijst2.append(i)
    return lijst2


def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    return (getTotalRentalCost(1,1)+ getJourneyFoodCostsInGold(1,1)+ getItemsValueInGold(gear))*len(getAdventuringInvestors(investors) )

        
##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int, COST_INN_HORSE_COPPER_PER_NIGHT, COST_INN_HUMAN_SILVER_PER_NIGHT:float) -> int:
    return int(leftoverGold//(copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)*horses + silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)* people))

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int, COST_INN_HORSE_COPPER_PER_NIGHT, COST_INN_HUMAN_SILVER_PER_NIGHT) -> float:
    return round(float(nightsInInn*(copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)*horses + silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)* people)),2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    lijst=[]
    for i in investors:
        lijst.append(round(profitGold/100*i['profitReturn'], 2))
    return list(lijst)

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    if round((profitGold - sum(investorsCuts))/ fellowship,2)>0:
        return round((profitGold - sum(investorsCuts))/ fellowship,2)
    else:
        return 0.0

##################### O14 #####################

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