"""
This class represents a fund to which contributors can donate.

Author: Sofie Aird
Date: 4/16/2024
"""
from donation import *
from datetime import date

class Fund(object):
    # implement the Fund class here
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.total = 0
        self.donations = []
    
    def getName(self):
        return self.name

    def getTarget(self):
        return self.target

    def getTotal(self):
        return self.total

    def getDonations(self):
        return self.donations

    def donate(self, contributor, amount):
        if (contributor == "" or amount <= 0):
            return False
        else:
            donation = Donation(contributor, str(date.today()), amount)
            self.donations.append(donation)
            self.total = self.total + amount
            return True

    def __str__(self):
        return "%s; target: %.2f; current total: $%.2f (%d%% reached)" % \
        (self.name, self.target, self.total, ((self.total/self.target)*100))

def main():
    fund = Fund("Toys", 50.0)
    print("name: " + fund.getName())
    print("target: %f" % (fund.getTarget()))
    print(fund)
    print(fund.donate("Jojo", 12.0))
    print(fund.getTotal())
    print(fund.donate("Jimmy", -3.50))
    print(fund.getTotal())
    print(fund.donate("", 12.0))
    print(fund.getTotal())
    print(fund)

    

if __name__ == '__main__':
    main()
