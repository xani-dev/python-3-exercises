import numpy as np
from students.stu0.ValidationException import ValidationException


def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")


def ex3():
    total_words = create_files("words.txt")
    print(f"Total words: {total_words}.")







#
# Your functions here...
#

def validate_file(file_name):
    with open(file_name, "r") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            parts = line.split(",")
            try:
                if parts[1].strip() != 'Miles':
                    n_miles = int(parts[1])
            except ValueError as ve:
                raise ValidationException(f"Invalid mileage: {parts[1]}")



def find_total_visits():
    # names = np.loadtxt("week-1.csv", delimiter=",", dtype=str)[:, 0:1]
    a1 = np.loadtxt("week-1.csv", delimiter=",", dtype=str)[1:4, 1:].astype(int)  # load, slice and cast.
    a2 = np.loadtxt("week-2.csv", delimiter=",", dtype=str)[1:4, 1:].astype(int)
    a3 = np.loadtxt("week-3.csv", delimiter=",", dtype=str)[1:4, 1:].astype(int)
    sum_array = a1 + a2 + a3
    return np.sum(sum_array)


def create_files(file):
    retval = 0
    lines = []
    large_words = set()
    small_words = set()
    with open(file, "r") as in_file:
        while True:
            line = in_file.readline()
            if not line:
                break
            lines.append(line)

    for line in lines:
        words = line.split(" ")
        for word in words:
            if word != '':
                if len(word) < 3:
                    small_words.add(word)
                else:
                    large_words.add(word)

    with open("large-words.txt", "w") as out_file1:
        for word in large_words:
            out_file1.writelines(f"{word}\n")

    with open("small-words.txt", "w") as out_file2:
        for word in small_words:
            out_file2.writelines(f"{word}\n")

    return len(large_words) + len(small_words)

