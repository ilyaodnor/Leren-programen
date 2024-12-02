# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # getal 1 is niet priemgetal
    if number <= 1:
        return False
    
    # getal 2 is priemgetal
    if number == 2:
        return True
    
    # Alle andere even getallen zijn geen priemgetallen
    if number % 2 == 0:
        return False
    
    #Controleer alleen oneven getallen tot aan de vierkantswortel van het getal
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    #  # Als er geen delers zijn gevonden, is het getal een priemgetal
    return True


def primes_up_to(n: int) -> list:
  return [i for i in range(2, n + 1) if is_prime(i)]


def aantal_primenumbers_tm(count: int)->list:
    primes = []
    number = 2 
    for i in range(count):
        if is_prime(number):
            primes.append(number)
        number+=1
    return primes

def primenumbers_tussen(a: int, b:int)->list:
    lijst = []
    for i in range(a,b+1):
        if is_prime(i) == True:
            lijst.append(i)

    return lijst
