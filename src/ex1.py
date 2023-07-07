from ValidationException import ValidationException


def validate_file(filename):
    print("Opening", filename)
    with open(filename, "r") as in_stream:
        for line_number, line in enumerate(in_stream, start=1):
            if line_number == 1:
                continue  # Skip the header line

            # Extract the car ID and mileage from the line    
            car_id, mileage = line.strip().split(',')

            try:
                # Convert mileage to an integer
                mileage = int(mileage)
            except ValueError:
                # If mileage is not a valid integer, raise a ValidationException
                raise ValidationException(f"Invalid mileage: {mileage} at line {car_id}")


def ex1():
    try:
        validate_file("../files/input.txt")
    except ValidationException as ve:
        print(ve)


ex1()