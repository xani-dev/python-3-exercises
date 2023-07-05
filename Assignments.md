# Python Intro III Assignments
***Submit a PR for each exercise then switch driver/navigator roles***
The structure of your work is up to you. I suggest creating a new file for each exercise.
And then copy paste the usage into each file and run that individually.

# Ex. 1 Validation Exception
Create a function called `validate_file()` which accepts a name of a file to validate.  This function validates the
[input.txt](files/input.txt) file and checks that the mileage for each car is a valid integer number.  This function
raises (throws) a `ValidationException` object and is consumed in the following manner:

Usage:
```python
def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)

ex1()
```

Output:
```
Invalid mileage:  32.13
```

# Ex. 2 Total Gym Visits
A gym has a weekly process that creates a CSV file for all the gym members.  This file indicates if a member has checked
into the gym for each day of the week.

Example file:
```
Name, S, M, T, W, Th, F, S
Alice, 1, 1, 0, 0, 1, 0, 1
Bob, 0, 0, 0, 0, 0, 0, 0
Charlie, 0, 0, 1, 0, 0, 1, 0
```

Create a function called `find_total_visits()` that calculates the total number of gym visits for the data in the following files:
- [week-1.csv](files/week-1.csv)
- [week-2.csv](files/week-2.csv)
- [week-3.csv](files/week-3.csv)

The function is consumed in the following manner:

Usage:
```python
def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()
```

Output:
```
Total visits: 21.
```

# Ex. 3 Word Counter I/O
Create a Python function called `count_words()` that accepts the name of an input file.  This function creates two files:
`large-words.txt` and `small-words.txt`.  The small words text file contains words that have less than 3 characters.  The 
large words text file contains words that are three characters or larger.  This function returns the total number of 
unique words. 

This function parses this [words.txt](files/words.txt) file and is used in the following manner:

Usage:
```python
def ex3():
    total_words = count_words("words.txt")
    print(f"Total words: {total_words}.")

ex3()
```

Output:
```
Total words: 16.
```

large-words.txt:
```
extremely
How
second
This
many
the
are
line.

words
this
file?

test.
large
```

small-words.txt:
```
in
a
is
```

# Ex. 4 Calculator Log S3
Create a function called `calculate()` that prompts the user to enter two numbers and returns displays the sum.  When the
user presses 'q' (for quit), the program uploads a file to S3 that contains a log of all the calculations.

Example usage:
```
Enter first number: 1
Enter first number: 2
1 + 2 = 3
Enter first number: 2
Enter first number: 2
2 + 2 = 4
Enter first number: q
*** Uploaded to S3 ***
```

The program uploads a file called `calculator-log.txt` that contains the log of all the calculations to an S3 bucket.  
Append your student id to the file name.

File:
```
1 + 2 = 3
2 + 2 = 4
```

Usage:
```python
def ex4():
    calculate()

ex4()
```

# Ex. 5 Car List*
Create a function called `build_car_list()`.  This function reads from the [input.txt](files/input.txt) file and reads from the
[car-ids.txt](files/car-ids.txt) file to build a single list of cars and removes the bad mileage data.

Output:
```python
[{'id': 1, 'miles': 10111, 'model': 'Ford'},
 {'id': 2, 'miles': 30333, 'model': 'Chevy'},
 {'id': 3, 'miles': 40443, 'model': 'Toyota'},
 {'id': 5, 'miles': 60000, 'model': 'Nissan'}]
```

Usage:

```python
def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
```
*This is a hard one.
