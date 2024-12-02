from math_operations import afronden
from test_lib import test, report

muntje= 14.88
expect_content=14.9
calculated_content=afronden(muntje)
name = f'Muntje: {muntje}'
test(name, expect_content, calculated_content )

muntje= 76.61
expect_content=76.60
calculated_content=round(afronden(muntje),2)
name = f'Muntje: {muntje}'
test(name, expect_content, calculated_content )

muntje= 28.82
expect_content=28.80
calculated_content=afronden(muntje)
name = f'Muntje: {muntje}'
test(name, expect_content, calculated_content )

muntje= -82.85
expect_content=-82.85
calculated_content=round(afronden(muntje), 2)
name = f'Muntje: {muntje}'
test(name, expect_content, calculated_content )

muntje= 149.69
expect_content=149.70
calculated_content=round(afronden(muntje),2)
name = f'Muntje: {muntje}'
test(name, expect_content, calculated_content )

muntje= 2.23
expect_content=2.25
calculated_content=afronden(muntje)
name = f'Muntje: {muntje}'
test(name, expect_content, calculated_content )



report()


