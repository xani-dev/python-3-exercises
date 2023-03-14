import numpy as np


def ex1():
    total = find_total_visits()
    print(f"Total visits: {total}.")


def ex2():
    total_words = create_files("words.txt")
    print(f"Total words: {total_words}.")


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

