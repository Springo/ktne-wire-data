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
from KTNEEngrModels import KTNEEngrModels

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
        header = ['wire_count',
                  'wire_1',
                  'wire_2',
                  'wire_3',
                  'wire_4',
                  'wire_5',
                  'wire_6',
                  'red_wire_count',
                  'blue_wire_count',
                  'yellow_wire_count',
                  'white_wire_count',
                  'black_wire_count',
                  'serial_number'
                  ]
        if labels:
            header.append('cut_wire')
        writer.writerow(header)
        for i in range(len(data)):
            writer.writerow(data[i])

def accuracy(labels, true_labels):
    cor = 0
    for i in range(len(true_labels)):
        if labels[i] == true_labels[i]:
            cor += 1
    return cor / len(true_labels)

def main():
    """ Main method for initializing a run """

    KW = KTNEWires()
    KWM = KTNEEngrModels()
    data = KW.generate_data(10000, labels=False)
    true_labels = KW.get_labels(data)
    rand_labels = KWM.random_predict(data)
    rand_n_labels = KWM.random_n_predict(data)
    mle_labels = KWM.mle_predict(data)
    mle_n_labels = KWM.mle_n_predict(data)
    engr_labels = KWM.engr_predict(data)
    print("Accuracies")
    print("Random: {}".format(accuracy(rand_labels, true_labels)))
    print("Random Given N: {}".format(accuracy(rand_n_labels, true_labels)))
    print("MLE: {}".format(accuracy(mle_labels, true_labels)))
    print("MLE Given N: {}".format(accuracy(mle_n_labels, true_labels)))
    print("Mechanized: {}".format(accuracy(engr_labels, true_labels)))

if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
