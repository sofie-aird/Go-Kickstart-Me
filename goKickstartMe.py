"""
This program allows the user to view and manage funds and donations.

Author: [your name]
Date: [today's date]
"""

from donation import *
from fund import *


def main():
    funds = initialize("funds.txt", "donations.txt")
    # implement the rest of the main function here



def initialize(fund_file, donation_file):
    """
    Reads the input files to initialize funds and their donations.

    Parameters:
    * fund_file: the name of the file containing info about the funds.
    * donation_file: the name of the file containing info about the donations.

    Returns: a list of Fund objects
    """
    print("In initialize")
    # implement the rest of the function here
    return [] # remove this after completing the implementation


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
            if(ls[j] < ls[smallest]):
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
