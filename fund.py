"""
This class represents a fund to which contributors can donate.

Author: [your name]
Date: [today's date]
"""
from donation import *
from datetime import date

class Fund(object):
    # implement the Fund class here

def main():
    fund = Fund("Toys", 50.0)
    print("name: " + fund.getName())
    print("target: %f" % (fund.getTarget()))

if __name__ == '__main__':
    main()
