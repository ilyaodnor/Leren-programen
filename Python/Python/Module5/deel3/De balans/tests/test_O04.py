import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

expect = 11
test('test days: ', expect, JOURNEY_IN_DAYS)


if __name__ == "__main__":
    report()