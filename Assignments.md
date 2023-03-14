# Python Intro III Assignments
Submit a PR for each exercise.

# Ex. 1 ValidationException
Create a function called `validate_file()` which accepts a name of a file to validate.  This function validates the
[input.txt](./input.txt) file and checks that the mileage for each car is a valid integer number.  This function
raises (throws) a `ValidationException` object and is consumed in the following manner:

```
def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)
```

Output:
```
Invalid mileage:  32.13
```



# Ex. 2 Total Gym Visits
A gym has a weekly process that creates a CSV file for all the gym members.  The CSV file contains the member name and a
1 if they have visited the gym, else a 0 for every day of the week:

```
Name, S, M, T, W, Th, F, S
Alice, 1, 1, 0, 0, 1, 0, 1
Bob, 0, 0, 0, 0, 0, 0, 0
Charlie, 0, 0, 1, 0, 0, 1, 0
```

Create a function called `find_total_visits()` that calculates the total number of gym visits from the data in the following files:
- [week-1.csv](week-1.csv)
- [week-2.csv](week-2.csv)
- [week-3.csv](week-3.csv)

The function is consumed in the following manner:

```python
def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")
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

This function parses this [words.txt](./words.txt) file and is used in the following manner:

```python
def ex3():
    total_words = count_words("words.txt")
    print(f"Total words: {total_words}.")
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

# Ex. 4 Todo...





