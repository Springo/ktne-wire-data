"""
AUTHORS: Kevin Xia

PURPOSE:
    Creating data based on the wire module from Keep Talking and Nobody Explodes

DEVELOPER NOTES:
    Author and program are not affiliated with KTNE in any way.
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import csv

# =============================================================================

class KTNEWires:
    """ KTNE wire data class """

    def __init__(self):
        """ Initialize fields here """

    def get_data(self, filename, head=True):
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

