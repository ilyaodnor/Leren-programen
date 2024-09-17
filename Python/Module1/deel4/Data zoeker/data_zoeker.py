from test_lib import *
from function import get_value


toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
value = get_value(toets_data, separator=',', position=0)
expected = 'Sofie:8'
name= f'Toets data: {expected}, value: {value}'
test(name, expected, value)



toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
value = get_value(toets_data, separator=',', position=1)
expected = 'Emma:7'
name= f'Toets data: {expected}, value: {value}'
test(name, expected, value)

toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
value = get_value(toets_data, separator=',', position=4)
expected = 'Lisa:8'
name= f'Toets data: {expected}, value: {value}'
test(name, expected, value)

toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
value = get_value(toets_data, separator=',', position=7)
expected = 'Ayoub:6'
name= f'Toets data: {expected}, value: {value}'
test(name, expected, value)

toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
value = get_value(toets_data, separator=',', position=2)
expected = 'Ahmed:9'
name= f'Toets data: {expected}, value: {value}'
test(name, expected, value)
report()
