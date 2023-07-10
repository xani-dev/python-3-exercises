import csv


def find_total_visits():
   #Reading from each file: 
    files = [f"../files/week-1.csv", f"../files/week-2.csv", f"../files/week-3.csv"]
    
    #Initializing Number of visits to Zero
    total_visits = 0
    
    #Reading from each file as read only ('r'):
    for every_file in files:
        with open(every_file, 'r') as file:
            
            #Using 'next' Py bult-in function to iterate thru items 
            next(file)
            
            #Reading line by line on each csv
            rows = csv.reader(file, delimiter=',')
            # reader =  csv.DictReader(file)
            # print(reader)
            for row in rows:
                print(row)
                for value in row[1:]:
                    
                    #Considering only Integers to do calculations: 
                    if int(value) == 1:
                        total_visits += 1
                        print('total visits so far: ' ,total_visits)
    return total_visits



def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()


