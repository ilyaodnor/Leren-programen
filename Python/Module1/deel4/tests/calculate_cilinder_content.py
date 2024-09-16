from math_operations import calculate_cilinder_content, add, divide, multiply
from test_lib import test, report
diameter =  8.0
height = 5.0
expect_content  = 251.3
calculate_content  = round(calculate_cilinder_content(diameter,  height), 1)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculate_content)

diameter =  11.0
height = 7.0
expect_content  = 665.2
calculate_content  = round(calculate_cilinder_content(diameter,  height), 1)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculate_content)

diameter =  18.0
height = 7.0
expect_content  =1781.3
calculate_content  = round(calculate_cilinder_content(diameter,  height), 1)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculate_content)

diameter =  15.0
height = 2.0
expect_content  = 353.4
calculate_content  = round(calculate_cilinder_content(diameter,  height), 1)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculate_content)

diameter =  0.0
height = 6.0
expect_content  = 0.0
calculate_content  = round(calculate_cilinder_content(diameter,  height), 1)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculate_content)

report()