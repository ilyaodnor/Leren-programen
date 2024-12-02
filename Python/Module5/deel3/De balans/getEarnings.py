from functions import*

def getEarnigs(profitGold: float, mainCharacter: dict, friends: list, investors: list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    
    interestingInvestors = getInterestingInvestors(investors)
    adventuringFriends = getAdventuringFriends(friends)
    adventuringInvestors = getAdventuringInvestors(investors)

    investorsCuts = getInvestorsCuts(profitGold, interestingInvestors)
    totalInvestorCut = sum(investorsCuts)
    
    fellowship = 1 + len(adventuringFriends) + len(adventuringInvestors)
    
    adventurerCut = round((profitGold - totalInvestorCut) / fellowship, 2)

    for person in people:
        startGold = getPersonCashInGold(person['cash'])
        endGold = startGold
        
       
        if person in interestingInvestors:
            index = interestingInvestors.index(person)
            endGold += investorsCuts[index]
        
       
        elif person in adventuringFriends or person in adventuringInvestors:
            endGold += adventurerCut
        if person == mainCharacter:
            endGold += adventurerCut
            endGold += 10 * len(adventuringFriends)  

     
        if person in adventuringFriends:
            endGold -= 10

        earnings.append({
            'name': person['name'],
            'start': round(startGold, 2),
            'end': round(endGold, 2)
        })

    return earnings
