'''
Create a function called build_car_list(). This function 
reads from the input.txt file and reads from the car-ids.txt
file to build a single list of cars and removes the bad mileage data.
'''
from pprint import pprint


def build_car_list(): 
    car_list = []

    # Read car models from car-ids.txt
    car_models = {}
    car_mileage = {}
    with open("../files/car-ids.txt", "r") as car_file:
        for line in car_file:
            car_id, model = line.strip().split(", ")
            car_models[car_id] = model

    # Read mileage data from input.txt
    with open("../files/input.txt", "r") as mileage_file:
        for line_number, line in enumerate(mileage_file, start=1):
            if line_number == 1:
                continue  # Skip the header line

            # Extract the car ID and mileage from the line    
            car_id, mileage = line.strip().split(',')
            car_mileage[car_id] = mileage
            
            try:
                mileage = int(mileage)
            except ValueError:
                continue
   
            if car_id in car_mileage:
                car = {"id": int(car_id), "miles": car_mileage[car_id], "model": car_models[car_id]}
                car_list.append(car)

    return car_list
          

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()