from ValidationException import ValidationException


def validate_file():
    pass # TODO



def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)

ex1()