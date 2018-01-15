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
from random import randint

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

    def generate_data(self, n, labels=True, n_wires=-1):
        """ Generates random KTNE data """

        data = []
        for i in range(n):
            if n_wires == -1:
                n_wir = randint(3, 6)
            else:
                n_wir = n_wires
            colornums = [randint(0, 4) for _ in range(6)]
            colors = ["none"] * 6
            n_red = 0
            n_blue = 0
            n_yellow = 0
            n_white = 0
            n_black = 0
            for j in range(n_wir):
                if colornums[j] == 0:
                    colors[j] = 'red'
                    n_red += 1
                elif colornums[j] == 1:
                    colors[j] = 'blue'
                    n_blue += 1
                elif colornums[j] == 2:
                    colors[j] = 'yellow'
                    n_yellow += 1
                elif colornums[j] == 3:
                    colors[j] = 'white'
                    n_white += 1
                else:
                    colors[j] = 'black'
                    n_black += 1
            serial = randint(0, 9)
            row = [n_wir]
            row.extend(colors)
            row.extend([n_red, n_blue, n_yellow, n_white, n_black, serial])
            data.append(row)

        if labels:
            labs = self.get_labels(data)
            for i in range(n):
                data[i].append(labs[i])

        return data

    def get_labels(self, data):
        """ Returns true labels to given KTNE data """

        labels = []
        for row in data:
            n_wires = row[0]
            w1 = row[1]
            w2 = row[2]
            w3 = row[3]
            w4 = row[4]
            w5 = row[5]
            w6 = row[6]
            n_red = row[7]
            n_blue = row[8]
            n_yellow = row[9]
            n_white = row[10]
            n_black = row[11]
            serial = row[12]

            result = 0
            if n_wires == 3:
                if n_red == 0:
                    result = 2
                elif w3 == 'white':
                    result = 3
                elif n_blue > 1:
                    if w3 == 'blue':
                        result = 3
                    else:
                        result = 2
                else:
                    result = 3
            elif n_wires == 4:
                if n_red > 1 and serial % 2 == 1:
                    if w4 == 'red':
                        result = 4
                    elif w3 == 'red':
                        result = 3
                    else:
                        result = 2
                elif w4 == 'yellow' and n_red == 0:
                    result = 1
                elif n_blue == 1:
                    result = 1
                elif n_yellow > 1:
                    result = 4
                else:
                    result = 2
            elif n_wires == 5:
                if w5 == 'black' and serial % 2 == 1:
                    result = 4
                elif n_red == 1 and n_yellow > 1:
                    result = 1
                elif n_black == 0:
                    result = 2
                else:
                    result = 1
            elif n_wires == 6:
                if n_yellow == 0 and serial % 2 == 1:
                    result = 3
                elif n_yellow == 1 and n_white > 1:
                    result = 4
                elif n_red == 0:
                    result = 6
                else:
                    result = 4
            else:
                raise BadDataError

            if result < 1 or result > 6:
                raise BadResultError
            else:
                labels.append(result)

        return labels


class BadDataError(Exception):
    pass


class BadResultError(Exception):
    pass
