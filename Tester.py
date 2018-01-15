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

def main():
    """ Main method for initializing a run """

    KW = KTNEWires()
    data = KW.generate_data(100)
    for row in data:
        print(row)

if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
