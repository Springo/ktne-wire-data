"""
AUTHORS: Kevin Xia

PURPOSE:
    Engineering models for predicting wire data

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

from random import randint

# =============================================================================

class KTNEEngrModels:
    """ Engineered models for predicting wire data """

    def __init__(self):
        """ Initialize fields here """

    def random_predict(self, data):
        """ Predicts random wire """
        return [randint(1,6) for _ in range(len(data))]

    def random_n_predict(self, data):
        """ Predicts random wire given number of wires """
        return [randint(1,data[i][0]) for i in range(len(data))]

    def mle_predict(self, data):
        """ Predicts most likely wire """
        return [2 for _ in range(len(data))]

    def mle_n_predict(self, data):
        """ Predicts most likely wire given number of wires """
        labels = []
        for i in range(len(data)):
            n_wires = data[i][0]
            if n_wires == 3:
                result = 2
            elif n_wires == 4 or n_wires == 5:
                result = 1
            else:
                result = 4
            labels.append(result)
        return labels

    def engr_predict(self, data):
        """ Heuristical prediction approach """
        labels = []
        for i in range(len(data)):
            n_wires = data[i][0]
            n_red = data[i][7]
            n_blue = data[i][8]
            if n_wires == 3:
                if n_red == 0:
                    result = 2
                else:
                    result = 3
            elif n_wires == 4:
                if n_blue == 1:
                    result = 1
                else:
                    result = 2
            elif n_wires == 5:
                result = 1
            else:
                result = 4
            labels.append(result)
        return labels
