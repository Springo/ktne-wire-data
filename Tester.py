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

def write_results(filename, data, labels=True):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Wire Count',
                  'Wire 1',
                  'Wire 2',
                  'Wire 3',
                  'Wire 4',
                  'Wire 5',
                  'Wire 6',
                  'Red Wire Count',
                  'Blue Wire Count',
                  'Yellow Wire Count',
                  'White Wire Count',
                  'Black Wire Count',
                  'Serial Number'
                  ]
        if labels:
            header.append('Cut Wire')
        writer.writerow(header)
        for i in range(len(data)):
            writer.writerow(data[i])

def main():
    """ Main method for initializing a run """

    KW = KTNEWires()
    data = KW.generate_data(1000)
    write_results("mock_data_train.csv", data)

if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
