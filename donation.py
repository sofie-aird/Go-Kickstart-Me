"""
This class represents a single donation to a fund.

Author: [your name]
Date: [today's date]
"""

class Donation(object):
    # implement the Donation class here

# This code tests the Donation class methods.    
def main():
    donation = Donation("Bluey", "2024-04-05", 25.32)
    print(donation.getContributor())
    print(donation)

# This calls main only if it has not already been called elsewhere.
if __name__ == '__main__':
    main()
