"""
This program allows the user to view and manage funds and donations.

Author: Sofie Aird
Date: 4/16/2024
"""

from donation import *
from fund import *


def main():
    funds = initialize("funds.txt", "donations.txt")
    menu_options()
    choice = get_user_choice()
    while choice != 7:
        if choice == 1:
            menu_1(funds)
        elif choice == 2:
            menu_2(funds)
        elif choice == 3:
            menu_3(funds)
        elif choice == 4:
            menu_4(funds)
        elif choice == 5:
            menu_5(funds)
        elif choice == 6:
            menu_6(funds)
        menu_options()
        choice = get_user_choice() 
    
    print("Bye bye")


def get_user_choice():
    choice = int(input("What would you like to do? "))
    while choice < 1 or choice > 7:
        print("invalid selection")
        choice = int(input("What would you like to do? "))
    return choice

def menu_1(funds):
    if len(funds) == 0:
        print("There are no funds.")
    else:
        sort(funds)
        for i in range(len(funds)):
            print(funds[i])

def menu_2(funds):
    # Create name list
    existing_names = []
    for fund in funds:
        existing_names.append(fund.getName())
    # Get name and validate
    print("Creating new fund")
    name = input("What is the name of the new fund? ")
    while name == "" or name in existing_names:
        if name == "":
            print("Must enter a name for your fund.")
        else:
            print("A fund with that name already exists")
        name = input("What is the name of your new fund? ")

    # Get value and validate
    target = float(input("What is the fund's target amount? "))
    while target <= 0:
        print("Target value must be positive.")
        target = float(input("What is the fund's target amount? "))

    # Create a new Fund object
    new_fund = Fund(name, target)
    funds.append(new_fund)
    print("Successfully created a new fund.")

def menu_3(funds):
    print("Here are the funds:")
    # Sort
    sort(funds)
    # Display
    for i in range(len(funds)):
        print("%d: %s" % (i+1, funds[i].getName()))
    # Prompt
    choice = int(input("Please select a fund: "))
    while choice <= 0 or choice > len(funds):
        print("That is an invalid choice")
        choice = int(input("Please select a fund: "))
    # Print donations
    print("Here are the donations:")
    for i in range(len(funds[choice-1].getDonations())):
        print(funds[choice-1].getDonations()[i])

def menu_4(funds):
    print("Here are the funds:")
    # Sort
    sort(funds)
    # Display
    for i in range(len(funds)):
        print("%d: %s" % (i+1, funds[i].getName()))
    # Prompt
    choice = int(input("Please select a fund: "))
    while choice <= 0 or choice > len(funds):
        print("That is an invalid choice")
        choice = int(input("Please select a fund: "))
    # Get name and validate
    name = input("What is the contributor's name? ")
    while name == "":
        print("Name cannot be empty")
        name = input("What is the contributor's name? ")
    # Get value and validate
    donation = float(input("What is the contribution amount? "))
    while donation <= 0:
        print("Contribution must be positive.")
        donation = float(input("What is the contribution amount? "))
    # Donate method
    valid = funds[choice-1].donate(name, donation)
    if valid:
        print("Thank you for your donation!")
    
def menu_5(funds):
    # Get name and validate
    name = input("What is the contributor's name? ")
    while name == "":
        print("Name cannot be empty")
        name = input("What is the contributor's name? ")
    print("Here are the donations: ")
    num_of_donations = 0
    total = 0
    for fund in funds:
        donations = fund.getDonations()
        for donation in donations:
            if donation.getContributor() == name:
                print("$%.2f to %s on %s" % (donation.getAmount(), \
                fund.getName(), donation.getDate()))
                num_of_donations += 1
                total += donation.getAmount()

    if num_of_donations == 0:
        print("This contributor has not made any donations")
    else:
        print("%s has made %d donations for a total of $%.2f" % (\
        name, num_of_donations, total))

def menu_6(funds):
    print("Extra credit.")

def menu_options():
    print("""
    ================== Menu ======================
1: list all funds
2: create a new fund
3: list donations for a fund
4: make a donation
5: list donations for a contributor
6: list aggregate donations for a fund
7: quit""")
    print()

def initialize(fund_file, donation_file):
    """
    Reads the input files to initialize funds and their donations.

    Parameters:
    * fund_file: the name of the file containing info about the funds.
    * donation_file: the name of the file containing info about the donations.

    Returns: a list of Fund objects
    """
    # Funds file
    fund_objects = []
    f = open(fund_file, "r")
    if (f == None):
        print("Error opening file %s" % (filename))
        return None
    for line in f:
        fund_info = line.strip().split(',')
        name = fund_info[0]
        target = float(fund_info[1])
        fund_objects.append(Fund(name, target))
    
    # Donation file
    f = open(donation_file, "r")
    for line in f:
        donation_info = line.strip().split(',')
        fund_name = donation_info[0]
        contributor = donation_info[1]
        amount = float(donation_info[2])
        for fund in fund_objects:
            if fund.getName() == fund_name:
                fund.donate(contributor, amount)

    return fund_objects


def sort(ls):
    """
    This is an implementation of selection sort that you can use as
    a foundation for your solution for Option 1 (and others as needed).
    Note that you will need to modify this for sorting a list of objects!

    Parameter: ls (list) - list of elements to be sorted

    Returns: None; the list is sorted as a side effect.
    """
    for i in range(len(ls)):
        smallest = i
        for j in range(i+1, len(ls)):
            if(ls[j].getName() < ls[smallest].getName()):
                smallest = j
        swap(ls,i,smallest)

def swap(ls, i, j):
    """
    Helper method for selection sort implementation.
    Swaps the values of ls[i] and ls[j].
    """
    tmp = ls[i]
    ls[i] = ls[j]
    ls[j] = tmp

main()
