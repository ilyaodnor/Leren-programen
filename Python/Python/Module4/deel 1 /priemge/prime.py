from functions import* 
from test_lib import *
expected = False
result = is_prime(19872496)
test('TEST: is_prime(19872496)',expected, result)

expected = [2,3,5,7]
result = primes_up_to(8)
test('TEST: primenumbers_tm(8)',expected,result)

expected = 4
result = len(aantal_primenumbers_tm(8))
test('TEST: aantal_primenumbers_tm(8)',expected,result)

expected = [11,13,17,19,23,29]
result = primenumbers_tussen(10,30)
test('TEST: primenumbers_tussen(10,30)',expected,result)

if __name__ == "__main__":
    report()