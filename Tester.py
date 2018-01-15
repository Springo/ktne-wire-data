"""
AUTHORS: Kevin Xia

PURPOSE:
    Testing the KTNEWires class

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import csv
from KTNEWires import KTNEWires

# =============================================================================

def get_data(filename, head=True):
    """ Reads and returns data from file """

    data = []
    header = []
    with open(filename, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        if head:
            header = next(csv_reader)
        for line in csv_reader:
            data.append(line)
    return data, header

def main():
    """ Main method for initializing a run """

    KW = KTNEWires()
    data = KW.generate_data(100)
    for row in data:
        print(row)

if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
