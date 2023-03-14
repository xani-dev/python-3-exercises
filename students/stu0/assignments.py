import numpy as np
import csv
from pprint import pprint


def ex1():
    a = np.array([1, 2, 3])
    with open('week-1.csv') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            print(row)


#
# Your functions here...
#
