from calc_discount import *

from test_lib import *

price = 500
brand = 'Vespa'
expect_content=50.0
calculated_content=calc_discount(price,brand,month_discount_brands)
name = f'Price: {price}, Brand: {brand}'
test(name, expect_content, calculated_content )


price = 700
brand = 'Yamaha'
expect_content=0.0
calculated_content=calc_discount(price,brand,month_discount_brands)
name = f'Price: {price}, Brand: {brand}'
test(name, expect_content, calculated_content )


price = 840
brand = 'Honda'
expect_content=0.0
calculated_content=calc_discount(price,brand,month_discount_brands)
name = f'Price: {price}, Brand: {brand}'
test(name, expect_content, calculated_content )


price = 988
brand = 'Kymc'
expect_content=98.8
calculated_content=calc_discount(price,brand,month_discount_brands)
name = f'Price: {price}, Brand: {brand}'
test(name, expect_content, calculated_content )


price = 1300
brand = 'Yamama'
expect_content=130.0
calculated_content=calc_discount(price,brand,month_discount_brands)
name = f'Price: {price}, Brand: {brand}'
test(name, expect_content, calculated_content )

report()