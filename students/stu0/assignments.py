import boto3
import numpy as np
from pprint import pprint
from botocore.exceptions import ClientError
from students.stu0.ValidationException import ValidationException

car_dict = {}


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


def ex4():
    calculate()


def ex5():
    car_list = build_car_list()
    pprint(car_list)


#
# Your functions here...
#


def calculate():
    history = []

    while True:
        first_num = input("Enter first number: ")
        if first_num == "q":
            break;
        sec_num = input("Enter first number: ")
        if sec_num == "q":
            break;
        total = int(first_num) + int(sec_num)
        history_line = f"{first_num} + {sec_num} = {total}"
        history.append(history_line)
        print(history_line)

    with open("calculator-log.txt", "w") as out_file:
        for line in history:
            out_file.writelines(line)

    s3_client = boto3.client('s3')
    file = 'calculator-log.txt'
    bucket_name = 'sia-test-bucket'
    key_path = 'merged/stu0/calculator-log.txt'
    try:
        response = s3_client.upload_file(file, bucket_name, key_path)
    except ClientError as e:
        print(e)
    print('*** Uploaded to S3 ***')


def transform_car(m):
    try:
        a = m.split(',')
        int(a[1].strip())
        retval = {
            "id": int(a[0].strip()),
            "model": car_dict[int(a[0].strip())],
            "miles": int(a[1].strip())
        }
    except ValueError:
        retval = {}  # catches bad mileage data
    return retval


def filter_car(c):
    if 'miles' in c:
        return c


def build_car_list():
    miles = []
    with open("input.txt", "r") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            if "CarId" not in line:
                miles.append(line.strip())

    with open("car-ids.txt", "r") as file2:
        while True:
            line = file2.readline()
            if not line:
                break
            if "CarId" not in line:
                line_list = line.split(",")
                car_dict.update({int(line_list[0]): line_list[1].strip()})

    new_list = list(map(transform_car, miles))
    filtered_list = list(filter(filter_car, new_list))
    return filtered_list


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
