"""
This class represents a single donation to a fund.

Author: Sofie Aird
Date: 4/16/2024
"""

class Donation(object):
    # implement the Donation class here
    def __init__(self, name, date, amount):
        self.contributor = name
        self.date = date
        self.amount = amount
    
    def getContributor(self):
        return self.contributor

    def getDate(self):
        return self.date

    def getAmount(self):
        return self.amount

    def __str__(self):
        return "%s donated $%.2f on %s" % (self.contributor, self.amount, \
        self.date)

# This code tests the Donation class methods.    
def main():
    donation = Donation("Bluey", "2024-04-05", 25.32)
    print(donation.getContributor())
    print(donation)
    print(donation.getDate())
    print(donation.getAmount())
    donation2 = Donation("Jojo", "2019-05-23", 50.20)
    print(donation2.getContributor())
    print(donation2.getDate())
    print(donation2.getAmount())

# This calls main only if it has not already been called elsewhere.
if __name__ == '__main__':
    main()
