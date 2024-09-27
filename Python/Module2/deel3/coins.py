# name of student: Ilya
# number of student: 99083003
# purpose of program: 
# structure of program: 

coinValues = [50,20,10,5,2,1] #maakt een lijst met coins

toPay = int(float(input('Amount to pay: '))* 100) #input to pay in euro, convertation in cents
paid = int(float(input('Paid amount: ')) * 100) #paid input in cents
change = paid - toPay # change

returnedCoins = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

if change == 0:
  print('done')
else:

  while change > 0 and len(coinValues) > 0: #cycle goes untill we have change and coins

    coinValue = coinValues.pop(0) #delete first element of the list
    nrCoins = change // coinValue #The maximum number of coins of the current denomination for change is calculated

    if nrCoins > 0: #Als er munten van dit type kunnen worden teruggegeven
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = float(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #

      returnedCoins[coinValue] += nrCoinsReturned
      change -= nrCoinsReturned * coinValue ## Verminder het wisselgeld met het bedrag van de teruggegeven munten
       

if change > 0: #if change can not be returnd
  print('Change not returned: ', str(change) + ' cents') #Meld als er nog wisselgeld over is
else:
  print('done')

for coinValue, count in returnedCoins.items():
  if count > 0: 
    print(f'{count} munt(en) van {coinValue} cent.')