import numpy as np
import csv
from pprint import pprint


def ex1():
    total = find_total_visits()
    print(f"Total visits: {total}.")


#
# Your functions here...
#

def find_total_visits():
    # names = np.loadtxt("week-1.csv", delimiter=",", dtype=str)[:, 0:1]
    a1 = np.loadtxt("week-1.csv", delimiter=",", dtype=str)[1:4, 1:].astype(int)  # load, slice and cast.
    a2 = np.loadtxt("week-2.csv", delimiter=",", dtype=str)[1:4, 1:].astype(int)
    a3 = np.loadtxt("week-3.csv", delimiter=",", dtype=str)[1:4, 1:].astype(int)
    sum_array = a1 + a2 + a3
    return np.sum(sum_array)

