# PYTHON BASICS
# Paseltongue is the langiage of the serpants and those who can converse with them. It is a hissing, sibilant langiuage that is difficult for most to learn. An individual who can speak paseltongue is known as a Parselmouth. It is a very uncommon skill, and may be hereditary. Nearly all known Parselmpouths are descended from Salazar Sytherin. 

# Python Reserved words: False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# DATA TYPES AND OPERATORS
# Numeric Types: int, float, complex
x = 5           # int
y = 3.14        # float
z = 2 + 3j     # complex
print(type(x))
print(type(y))
print(type(z))

# Arithmetic Operators: +, -, *, /, //, %, **
a = 10
b = 3
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation
# Comparison Operators: ==, !=, >, <, >=, <=
print(a == b)   # Equal to
print(a != b)   # Not equal to
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to
# Logical Operators: and, or, not
print((a > b) and (a != b))  # Logical AND
print((a > b) or (a == b))   # Logical OR
print(not(a > b))             # Logical NOT

# TYPE CONVERSION: Type conversion is the process of converting a value from one data type to another. In python, we can use built-in functions to convert between different data types. eg:
x = 5           # int
y = 3.14        # float
z = '10'        # str
# Converting int to float
x_float = float(x)
print(x_float)  # Output: 5.0
# Converting float to int
y_int = int(y)
print(y_int)    # Output: 3
# Converting str to int
z_int = int(z)
print(z_int)    # Output: 10
# Converting int to str
x_str = str(x)
print(x_str)    # Output: 5
# Converting float to str
y_str = str(y)
print(y_str)    # Output: 3.14
# Converting str to float
z_float = float(z)
print(z_float)  # Output: 10.0

# TYPE PROMOTION: Type promotion is the automatic conversion of a value from one data type to another during an operation. In python, when we perform an operation between two different data types, python automatically promotes the lower data type to the higher data type. eg:
x = 5           # int
y = 3.14        # float
# Adding int and float
result = x + y
print(result)   # Output: 8.14
print(type(result))  # Output: <class 'float'>
# In the above example, python automatically promotes the int value of x to a float value before performing the addition operation.

# Type Casting: Type casting is the explicit conversion of a value from one data type to another using built-in functions. eg:
x = 5           # int
y = 3.14        # float
# Casting int to float
x_float = float(x)
print(x_float)  # Output: 5.0
# Casting float to int
y_int = int(y)
print(y_int)    # Output: 3


# VARIABLES, EXPRESSIONS and STATEMENTS
# Constants: Fixed values such as numbers, letter, and strings are called "constants" because their values does not change.
# Variables: A variable is a named location used to store data in the memory. The value of a variable can change during program execution. eg:
x = 12.2
y = 14


# A program to covert Europe floor to US floor
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

# Expressions: An expression is a combination of values, variables, and operators that computes to a value. eg: x + y is an expression that adds the values of x and y.  
z = x + y
print(z)

# Statements: A statement is a complete line of code that performs some action. eg: the assignment statement x = 12.2 assigns the value 12.2 to the variable x.
a = 5
b = 10
c = a+b
print(c)

# Comments: Comments are lines in a program that are not executed. They are used to explain the code and make it more readable. In python, comments starts with the # symbol.

# Conditional Execution: Conditional execution is used to perform different actions based on wether a condition is true or false. In python, conditional execution is implemented using the if, elif, and else statements. eg:
age = 20
if age < 18:
     print('You are a minor.')
else:
     print('You are an adult.')

# Try and Except structure: The try and except structure is used to handle errors and exceptions in a program. It allows the program to continue running even if an error occurs. eg:
astr = 'Jason'
try: 
     print('Hello')
     istr = int(astr)
     print('There') 
except:
     istr = -1
print('Done', istr)

# eg2:
rawstr = input('Enter a number:')
try: 
     ival = int(rawstr)
except:
     ival = - 1
if ival > 0:
     print('Nice work')
else:
     print('Not a number')

# FUNCTIONS: A function is a named block of code that performs a specific task. Functions are used to organize code and make it more reusable. In python, a function is a reusable code that takes argument(s) as input, do some computation, and returns a result. We call/invoke the function by using the function name, parentheses, and arguments in an expression. Functions are defined using the def keyword. 
# eg1:
def thing():
     print('Hello')
     print('There')
thing()
print('Zip')
thing()

# eg2:
def greet(lang):
     if lang == 'es':
          print('Hola')
     elif lang == 'fr':
          print('Bonjour')
     else: 
          print('Hello')
greet('en')
greet('es')
greet('fr')

# Types of Funcions in Python:
# Built-in functions: python provides a number of built-in functions that can be used to perform common tasks. eg: print(), input(), int(), str(), len(), type(),range(), sum(), max(), min() etc.

#  User-defined functions: Users can define their own functions to perform specific tasks. eg: greet(lang) function defined above. Other user defind functions include:Anonymous functions(lambda functions), Recursive functions, Higher-order functions, Generator functions.

# The return statement: the return statement is used to return a value from a function. When a return statement is eecuted, the function terminates and the value s returned to the caller. eg1:
def greeting():
     return 'Hello'
print(greeting(), 'Jason')

#  eg2
def addtwo(a,b):
     added = a + b
     return added

x = addtwo(3, 5)
print(x)

#LOOPS AND ITERATION: Loops are used to repeat a block of code multiple times. In python, loops are implemented using the for and while statements. eg: 
# eg1: Using a for loop to iterate over a list
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
     print(fruit)

# eg2: Using a while loop to print number from 1 to 5
count = 1
while count <= 5:
     print(count)
     count = count + 1

# eg3: Using while loop to print numbers from 5 to 1
n = 5
while n > 0:
     print(n)
     n = n - 1
     print('Blastoff!')
     print(n)

#  Breaking out of a Loop: The break statement is used to exit a loop prematurely. When a break ststement is executed, the loop terminates and the program continues with the next stetement after the loop. eg:
n = 0
while True:
     print(n)
     n = n + 1
     if n == 5:
          break
print('Done')
#  Continuing a Loop: The continue statement is used to skip the current iteration of a loop and move to the next iteration. When a continue statement is executed, the rest of the code in the loop is skipped for the current iteration, and the loop continues with the next iteration. eg:
for i in range(10):
     if i % 2 == 0:
          continue
     print(i)

# eg2:this program prints all odd numbers between 1 and 10
n = 0
while n < 10:
     n = n + 1
     if n % 2 == 0:
          continue
     print(n)

# Definite and indefinite loops:
# Definite loops: A definite loop is a loop that iterates over a sequence of values, such as a list or a range of numbers. The number of iterations is known before the loop starts. eg: for loop is a definite loop.
# Indefinite loops: An indefinite loop is a loop that continues to iterate until a certain condition is met. The number of iterations is not known before the loop starts. eg: while loop is an indefinite loop.
# eg1: Definite loop using for loop
for i in range(5):
     print(i)

# Loop ideoms: A loop idiom is a common pattern or technique used in programming to solve a specific problem using loops. eg:
# eg1: Summing a series of numbers using a loop 
total = 0
for i in range(1, 6):
     total = total + i
print('Total:', total)

# eg2: Finding the largest number in a list using a loop
numbers = [3, 5, 2, 8, 1]
largest = numbers[0]
for num in numbers:
     if num > largest:
          largest = num
print('Largest number:', largest)

# eg3: Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
     if the_num > largest_so_far:
          largest_so_far = the_num
     print(largest_so_far, the_num)
print('After', largest_so_far)

# Counting in a Loop:A common use of loops is to count the number of items that meet a certain condition.To count how many times we execute a loop, we introduce a counter variable thsat starts at 0 and we add one to it each time through the loop. eg:
zork = 0
print('Before', zork)
for number in [9, 41, 12, 3, 74, 15]:
     zork = zork + 1
     print(zork, number)

# Summing in a Loop: Another common use of loops is to compute a running total or sum of values. To compute a sum, we introduce an accumulator variable that starts at 0 and we add each value to it as we loop through the values. eg:
zork = 0
print('Before', zork)
for number in [9, 41, 12, 3, 74, 15]:
     zork = zork + number
     print(zork, number)
print('After', zork)

# Average in a Loop: To compute an average, we need to keep track of both the sum of the values and the count of the values. We can use two accumulator variables, one for the sum and one for the count. eg:
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
     count = count + 1
     sum = sum + value
     print(count, sum, value)
print('After', count, sum, sum / count)

# Filtering in a Loop: Sometimes we only want to process certain values in a loop based on a condition. We can use an if statement inside the loop to filter the values. eg:
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
     if value > 20:
          print('Large number', value)
print('After')

# Search using a Boolean Variable: We can use a boolean variable to keep track of whether we have found a certain value in a loop. If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for. eg:
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
     if value == 3:
          found = True
     print(found, value)
print('After', found)

# Finding the Smallest Value: To find the smallest value in a loop, we can use a variable to keep track of the smallest value found so far. We initialize this variable to None and update it whenever we find a smaller value. eg:
smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15]:
     if smallest is None :
       smallest = value
     elif value < smallest:
          smallest = value
     print(smallest, value)
print('After', smallest)

# Nested Loops: A nested loop is a loop that is contained within another loop. The inner loop is executed for each iteration of the outer loop. eg:
for i in range(3):
     for j in range(2):
          print(i, j)
# eg2: Nested loop to print a multiplication table
for i in range(1, 6):
     for j in range(1, 6):
          print(i * j, end='\t')
     print()

# STRINGS AND TEXT PROCESSING
# Strings: A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" "). Strings are used to represent text data in Python. eg:
message = "Hello, World!"
print(message)
# String Indexing: You can access individual characters in a string using indexing. The index of the first character is 0, the second character is 1, and so on. Negative indexing allows you to access characters from the end of the string, with -1 being the last character.
s = "Hello, World!"
print(s[0])   # Output: H
print(s[7])   # Output: W
print(s[-1])  # Output: !
print(s[-5])  # Output: o

# Looping through Strings: You can loop through each character in a string using a for loop. This allows you to access and manipulate each character individually.

fruit = "banana"
for letter in fruit:
    print(letter)

# Looping and Counting: You can use a loop to count the occurrences of a specific character in a string. This is useful for analyzing text data.
word = "banana"
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print('Number of a\'s:', count)

# Slicing Strings: Slicing allows you to extract a portion of a string by specifying the start and end indices. This is useful for obtaining substrings.
s = "Hello, World!"
print(s[0:5])  # Output: Hello
print(s[7:12]) # Output: World
print(s[:5])   # Output: Hello
print(s[7:])   # Output: World!
print(s[:])    # Output: Hello, World!

# String Comparison: You can compare strings using comparison operators such as ==, !=, <, >, <=, >=. String comparison is case-sensitive and based on the lexicographical order of characters.
str1 = "apple"
str2 = "banana"
if str1 < str2:
    print(f'"{str1}" comes before "{str2}"')
else:
    print(f'"{str1}" comes after "{str2}"')

# String Methods: Python provides several built-in string methods that allow you to manipulate and analyze strings. Some common string methods include lower(), upper(), strip(), replace(), find(), and split().
text = "  Hello, World!  "
print(text.lower())        # Output: "  hello, world!  "
print(text.upper())        # Output: "  HELLO, WORLD!  "
print(text.strip())       # Output: "Hello, World!"
print(text.replace("World", "Python"))  # Output: "  Hello, Python!
print(text.find("World"))  # Output: 8
print(text.split(","))     # Output: ['  Hello', ' World!  ']

# Parsing and Extracting: You can parse strings to extract specific information. This is often done using string methods or regular expressions.

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# Output: 21
sppos = data.find(' ', atpos)
print(sppos)
# Output: 31
host = data[atpos + 1:sppos]
print(host)
# Output: uct.ac.za

# FILE PROCESSING: A text file is a sequence of lines of text. Each line is terminated with a special character called a newline character. When you read a file, you get the newline character as part of the line. To remove the newline character from the end of the line, you can use the rstrip() method. eg:
fhand = open('example.txt')
for line in fhand:
     line = line.rstrip()
     print(line)
fhand.close()

# Opening Files: You can open files using the open() function, which returns a file object. You can then read from or write to the file using various methods.
file = open('example.txt', 'r') 
content = file.read()
print(content)
file.close()

# File Handles: A file handle is a or wrapper which is a reference to an open file. You can use the file handle to read from or write to the file. eg:
fhand = open('example.txt')
for line in fhand:
     print(line)
fhand.close()

# File Modes: When opening a file, you can specify the mode in which the file is opened. Common modes include 'r' for reading, 'w' for writing (which overwrites the file), and 'a' for appending (which adds to the end of the file).
# eg:
fhand = open('example.txt', 'w')  # Open file for writing
fhand.write('Hello, World!\n')
fhand.close()

# File Paths: A file path is a string that specifies the location of a file on the filesystem. It can be an absolute path (starting from the root directory) or a relative path (starting from the current working directory).
# eg:
fhand = open('C:/Users/JamesOrban/Desktop/Python/Python syntax/example.txt')
content = fhand.read()
print(content)
fhand.close()

# The newline Character: The newline character (\n) is a special character that represents the end of a line in a text file. When reading a file, each line will include the newline character at the end. You can use the rstrip() method to remove the newline character from the end of a line.
# eg:
line = "Hello, World!\n"
print(line.rstrip())  # Output: "Hello, World!"

# Reading Files Line by Line: You can read a file line by line using a for loop. This allows you to process each line individually. A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence. eg:
xfile = open('mbox.txt')
for line in xfile:
     print(line)

# Counting Lines in a File: You can count the number of lines in a file by iterating through each line and incrementing a counter variable. eg:
fhand = open('mbox.txt')
count = 0
for line in fhand:
     count = count + 1
print('Line count:', count)

# Reading the Entire File: You can read the entire contents of a file at once using the read() method. This returns the entire file as a single string. eg:
fhand = open('mbox.txt')
content = fhand.read()
print(len(content))
print(content[:20])  # Print the first 20 characters
fhand.close()

# Searching Through a File: We can put an if statement in our for loop to only print lines that meet a certain condition. eg:
fhand = open('mbox.txt')
for line in fhand:
     line = line.rstrip()
     if line.startswith('From:'):
          print(line)
fhand.close()

# Skipping Lines in a File: We can use the continue statement to skip lines that do not meet a certain condition. eg:
fhand = open('mbox.txt')
for line in fhand:
     line = line.rstrip()
     if not line.startswith('From:'):
          continue
     print(line)

# Prompting for a File Name: We can use the input() function to prompt the user for a file name. This allows us to open different files based on user input. eg:
fname = input('Enter file name: ')
fhand = open(fname)
count = 0
for line in fhand:
     if line.startswith('Subject:'):
          count = count + 1
print('There were', count, 'subject lines in', fname)

# Bad File Names: We can use a try and except block to handle errors when opening a file. This allows us to gracefully handle situations where the file does not exist or cannot be opened. eg:
fname = input('Enter file name: ')
try:
     fhand = open(fname)
except:
     print('File cannot be opened:', fname)
     quit()
count = 0
for line in fhand:
     if line.startswith('Subject:'):
          count = count + 1
print('There were', count, 'subject lines in', fname)

# DATA STRUCTUIRES: LISTS AND DICTIONARIES
# Algortihms: An algorithm is a step-by-step procedure or set of rules for solving a specific problem or performing a specific task. Algorithms are used in computer science and programming to design efficient and effective solutions to various problems. They can be expressed in various forms, such as natural language, pseudocode, or programming languages. eg: searching and sorting algorithms.

# Data Structures: Data structures are specialized formats for organizing, processing, and storing data in a computer so that it can be accessed and modified efficiently. Different types of data structures are suited to different kinds of applications, and some are highly specialized to specific tasks. eg: lists, dictionaries, sets, tuples etc.

# Collections: A collection is a data structure that groups multiple items together into a single unit. Collections are used to store and organize data in a way that allows for efficient access and manipulation. eg: lists, dictionaries, sets, tuples etc.

# PYTHON LISTS: A list is a collection of items that are ordered and changeable. Lists are defined using square brackets [] and items are separated by commas. eg:
fruits = ['apple', 'banana', 'orange']
print(fruits)
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: orange
fruits.append('grape')  # Adding an item to the list
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']
fruits.remove('banana')  # Removing an item from the list
print(fruits)  # Output: ['apple', 'orange', 'grape']

# List Constants: A list constant is a fixed value that represents a list of items. List constants are defined using square brackets [] and items are separated by commas. eg:
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]
mixed = [1, 'apple', 3.14, True]
print(mixed)  # Output: [1, 'apple', 3.14, True]

# Lists are Mutable: Lists are mutable, which means that their contents can be changed after they are created. You can add, remove, or modify items in a list using various methods. eg:
colors = ['red', 'green', 'blue']
colors[1] = 'yellow'  # Modifying an item in the list
print(colors)  # Output: ['red', 'yellow', 'blue']
colors.append('purple')  # Adding an item to the list
print(colors)  # Output: ['red', 'yellow', 'blue', 'purple']
colors.remove('red')  # Removing an item from the list
print(colors)  # Output: ['yellow', 'blue', 'purple']

# List Operations: Python provides several built-in methods and operations for working with lists. Some common list operations include:
# len(): Returns the number of items in a list.
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5
# sort(): Sorts the items in a list in ascending order.
numbers = [5, 2, 8, 1, 4]
numbers.sort()
print(numbers)  # Output: [1, 2, 4, 5, 8]
# reverse(): Reverses the order of items in a list.
colors = ['red', 'green', 'blue']
colors.reverse()
print(colors)  # Output: ['blue', 'green', 'red']
# index(): Returns the index of the first occurrence of a specified item in a list.
fruits = ['apple', 'banana', 'orange']
print(fruits.index('banana'))  # Output: 1
# count(): Returns the number of occurrences of a specified item in a list.
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # Output: 3
# append(): Adds an item to the end of a list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
# insert(): Inserts an item at a specified index in a list.
my_list = [1, 2, 3]
my_list.insert(1, 15)
print(my_list)  # Output: [1, 15, 2, 3]
# remove(): Removes the first occurrence of a specified item from a list.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]
# pop(): Removes and returns the item at a specified index in a list. If no index is specified, it removes and returns the last item.
my_list = [1, 2, 3]
item = my_list.pop(1)
print(item)     # Output: 2
print(my_list)  # Output: [1, 3]
# clear(): Removes all items from a list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
# copy(): Returns a shallow copy of a list.
original = [1, 2, 3]
copy_list = original.copy()
print(copy_list)  # Output: [1, 2, 3]

# Looping through a List: You can loop through each item in a list using a for loop. This allows you to access and manipulate each item individually. eg:
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
     print(fruit)
# eg2: Counting the number of items in a list
count = 0
for fruit in fruits:
     count = count + 1
print('Number of fruits:', count)

# Python Dictionaries: A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed. Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. eg:
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person)
print(person['name'])  # Output: John
print(person['age'])   # Output: 30
person['age'] = 31    # Modifying a value in the dictionary
print(person)         # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Dictionary Literals: A dictionary literal is a fixed value that represents a dictionary of key-value pairs. Dictionary literals are defined using curly braces {} and key-value pairs are separated by commas. eg:
car = {'make': 'Toyota', 'model': 'Camry', 'year': 2020}
print(car)  # Output: {'make': 'Toyota', 'model': 'Camry', 'year': 2020}

# Dictionaries are Mutable: Dictionaries are mutable, which means that their contents can be changed after they are created. You can add, remove, or modify key-value pairs in a dictionary using various methods. eg:
student = {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
student['age'] = 21  # Modifying a value in the dictionary
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}


# Dictionary Operations: Python provides several built-in methods and operations for working with dictionaries. Some common dictionary operations include:
# keys(): Returns a view object that contains the keys of the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])
# values(): Returns a view object that contains the values of the dictionary.

# The get method for dictionaries: The get() method is a built-in method in Python that is used to retrieve the value associated with a specified key in a dictionary. The get() method takes two arguments: the key to be searched for and an optional default value to be returned if the key is not found in the dictionary. If the key is found, the corresponding value is returned; otherwise, the default value (if provided) is returned. If no default value is provided and the key is not found, the method returns None.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('b'))        # Output: 2
print(my_dict.get('d', 4))     # Output: 4
print(my_dict.get('e'))        # Output: None

# Using the get() method to simplify counting occurrences of items in a list
# eg3: 
counts = dict()
names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
for name in names:
     counts[name] = counts.get(name, 0) + 1
print(counts)  # Output: {'Alice': 3, 'Bob': 2, 'Charlie': 1}

# Counting Words in a File: We can use a dictionary to count the occurrences of each word in a file. We read the file line by line, split each line into words, and update the count for each word in the dictionary. eg:
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('counting...')
for word in words:
     counts[word] = counts.get(word, 0) + 1

print('Counts:', counts)

# Definite Loops and Dictionaries: We can use a for loop to iterate through the key-value pairs in a dictionary. This allows us to access and manipulate each key-value pair individually. eg:
counts = {'apple': 2, 'banana': 3, 'orange': 1}
for key in counts:
     print(key, counts[key])

# eg2: Finding the most common word in a dictionary
bigcount = None
bigword = None
for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
print (bigword, bigcount)

# Retrieving lists of Keys and Values: We can use the keys() and values() methods to retrieve lists of keys and values from a dictionary. This allows us to access and manipulate the keys and values separately. eg:
jjj = {'a': 1, 'b': 2, 'c': 3}
print(list(jjj))         # Output: ['a', 'b', 'c']
print(list(jjj.keys()))    # Output: ['a', 'b', 'c']
print(list(jjj.values()))  # Output: [1, 2, 3]
print(jjj.items())      # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Two Iteration Variables: When iterating through a dictionary using the items() method, we can use two iteration variables to access both the key and the value of each key-value pair. This allows us to work with both the key and the value simultaneously. “This is a Pythonic feature that is especially concise and readable in Python, though similar destructuring mechanisms exist in some other programming languages.”. eg:
jjj = {'a': 1, 'b': 2, 'c': 3}
for k, v in jjj.items():
     print('Key:', k, 'Value:', v)

# Program to open a file, read it line by line, find the most common word and print the bigword and its count

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
print (bigword, bigcount)

# eg2:
# if name in counts:
#      x = counts[name]
# else:
#      x = 0
# x = counts.get(name, 0)

# Tuples are immutable: Once a tuple is created, its elements cannot be changed, added, or removed. eg:
z = (5, 6, 7)
# z[0] = 10  # This will raise a TypeError
print(z)
# However, you can create a new tuple that combines elements from existing tuples:
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)  # Output: (1, 2, 3, 4, 5, 6)
# Tuples can be used as keys in dictionaries: Since tuples are immutable, they can be used as keys in dictionaries, unlike lists. eg:
my_dict = {('a', 1): 'value1', ('b', 2): 'value2'}
print(my_dict[('a', 1)])  # Output: value1
# Tuples can be unpacked: You can assign the elements of a tuple to individual variables in a single statement. eg:
person = ('Alice', 30, 'Engineer')
name, age, profession = person
print(name)        # Output: Alice
print(age)         # Output: 30
print(profession)  # Output: Engineer

# Sorting Lists of Tuples: You can sort a list of tuples based on the elements of the tuples. By default, Python sorts tuples lexicographically, meaning it compares the first elements, and if they are equal, it compares the second elements, and so on. We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary. First, we sort the dictionary by the key using the items() method and sorted() function.eg:
d = {'a': 3, 'b': 1, 'c': 2}
d.items()  # Output: dict_items([('a', 3), ('b', 1), ('c', 2)])
sorted(d.items())  # Output: [('a', 3), ('b', 1), ('c', 2)]
for k, v in sorted(d.items()):
     print(k, v)
# To sort the dictionary by value, we can create a list of tuples where each tuple contains the value and the key. We can then sort this list of tuples to get the desired order. eg:
d = {'a': 3, 'b': 1, 'c': 2}
tmp = list()
for k, v in d.items():
     tmp.append((v, k))
print(tmp)  # Output: [(3, 'a'), (1, 'b'), (2, 'c')]
tmp = sorted(tmp, reverse=True)   
print(tmp)  # Output: [(3, 'a'), (2, 'c'), (1, 'b')]

# eg2: Program to read through a file and build a histogram of the counts of each word using a dictionary. Then we convert the dictionary into a list of tuples and sort the list in reverse order based on the count. Finally, we print the top 10 most common words along with their counts.
# name = input('Enter file:')
handle = open('romeo.txt')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#print(sorted([(v, k) for k, v in d.items()])) 
lst = list()
for key, val in counts.items():
    lst.append((val, key))
lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

# Regular Epression: Regular expressions are cryptic but powerful language for matching strings and extracting elements from those strings. They have special characters that indicate intent.

# eg1: Using re.search() like find() in a list.

import re
hand = open('mbox-short.txt')
for line in hand:
     line = line.rstrip()
     if re.search('From:', line):
          print(line)

# Matching and Extracting Data
# re.search returns a True/False depending on wether the string matches the regular expression
# if we actually want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)  # Result ['2', '19', '42']
z = re.findall('[AEIOU]+',x)
print(z) # Result into an empty list []

# Greedy Matching: The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string.
import re
x = 'From: Using the : character'
y = re.findall('F.+:', x)
print(y)

# Non-Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('F.+?:', x)
print(y)

# program to extract spam from and email(spam confidence)

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
     line = line.strip()
     stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
     if len(stuff) != 1 : continue
     num = float(stuff[0])
     numlist.append(num)
print('Maximum:', max(numlist)) # Maximum = 0.9907

# NETWORKED PROGRAMS

# TCP(Transmission Control Protocol) Connections/Sockets: In computer networking, an internet socket or network socket is an endpoint of a bidirctional inter-process communication flow across an internet Protocol-based compuetr network, such as the internet.

# TCP Port Numbers: A port is an application-specific or process-specific software communication endpoint. it allows multiple networked applications to coexist on the same server. There are a list of well-known TCP port numbers.
# Common TCP Ports: Telnet(23)-Login, SSH(22)-secure login, HTTP(80), HTTPS(443)-secure,SMTP(25)(mail), IMAP(143/220/993)- Mail Retrieval, POP(109/110)- Mail Retrieval, DNS(53)-Dormain Name, FTP(21)-File Transfer. 

# Sockets in Python: Python has built-in support for TCP Sockets

import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))

# Application Protocol: 
# HTTP=Hypertext Transfer Protocol: The dorminant application layer protocol on the internet. Invented for the Web-to retrieve HTML, images, Documents etc. Extended to be data in addition tpo documents - RSS, Web services, etc. Basic concept= Make a conncetion-Request a document-Retrieve the document-Close the connection.
# HTTP: The HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents from servers over the internet. A protocol is a set of rules that all parties follow so we can predict each other's behavior. URL:A URL (Uniform Resource Locator) is the unique web address (like https://www.example.com/page) used to find and access resources (web pages, images, files) on the internet, telling browsers the protocol (how to connect), the domain name (where it is), and the specific path (which file) needed, acting as a digital address for online content. 

# An HTTP Request in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
mysock.send(cmd)

while True:
     data = mysock.recv(512)
     if (len(data) < 1):
          break
     print(data.decode())
mysock.close()

# Multi-Byte Characters: To represent the wide range of characters computers must handle we represent characters with more than one byter. UTF-16 = Fixed length-Two bytes, UTF-32 = Fixed Length - Four bytes, UTF-8 = 1-4 bytes. Upwards compatible with ASCII. Automatic detection between ASCII and UTF-8. UTF-8 is recommended practice for encoding data to be exchanged between systems.

# UNICODE SUPPORT: The greatest difference between Python 2 and Python 3 is that, in Python 2, bytes and strings were thesame and unicode seperate, while in python 3, strings and unicode are thesame while bytes are difference.
# In Python 2, every single Unicode string has to be marked with a “u” prefix as it uses ASCII characters by default. By contrast, Python 3 stores strings as Unicode by default, which is more versatile than ASCII strings. When sending data to a network, you must encode()into UTF-8 to get a byte array why receiving data from a network, you most decode() to get a string array.

# Using urllib in Python: Since HTTP is so common, we have a library that does all the socket work for us and make web pages look like a file.

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
     print(line.decode().strip())

# Retrieving like a file, a dictionary

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
     words = line.decode().split()
     for word in words:
          counts[word] = counts.get(word,0) + 1
print(counts)

# Reading Web Pages

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
     print(line.decode().strip())

# Web Scraping: When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web pages. Search engines scrape web pages-we call this 'spidering the web' or 'web crawling'

# Why Scrape? Pull data- particularly socio data- who links to who?, Get your own data back ou of some system that has no 'export capability', Monitor a site for new information, Spider the web to make a database for a search engine.

# The Easy Way - Beautiful Soup: You could do string searches the hard way. Or use the free software library called BeautifulSoup from www.crummy.com
# BeautifulSoup Installation
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# or download the file
# http://www.py4e.com/code3/bs4.zip and unzip it in the same directory as this file.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter the url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the archor tags
tags = soup('a')
for tag in tags:
     print(tag.get('href', None))


# WEB SERVICES
# Data on the Web: With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols. We needed to come up with an agreed way to represent data going between applications and across networks. There are two dommonly used formats: XML and JSON

# Wire Protocol: it is a protocol that is independent, it is what we send on the wire. 
# A wire protocol defines the rules for how applications communicate over a network, specifying the format, sequence, and encoding of data (messages) sent between systems, ensuring different software can interoperate, often at the application (Layer 7) level, distinct from underlying transport protocols like TCP/UDP. Examples include protocols for databases (PostgreSQL), debuggers (JDWP), and general distributed systems (SOAP, Wayland). 
# XML=eXtensible Markup Language, Marking up data to send across the network. The primary purpose is to help information system share structured data. It started as a simpliified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible

# XML Shema: Description of the legal format of an XML document. Expressed in terms of constraints on the structure and content of documents. Often use to specify a 'contract' between systems- 'My system will only accept XML that conforms ot this paricular schema.If a particular piece of XML meets the specification of the Schema- it is said to 'validate'

# JavcaScript Object Notation: Object literal notation in JavaScript. JSON represents data as nested lists and dictionaries.

import json
data = '''{
    "name" : "Jason",
     "phone" : {
    "type" : "int",
    "number" : "+234 75395017"
   },
   "email" : {
     "hide" : "yes"
   } 
}'''

info = json.loads(data)
print('Name:',info['name'])
print('Hide:',info['email']['hide'])

# Service Oriented Approach: Most non-trivial web applications use services. They use services from other applications. Credit Card Charge, Hotel Reservation Systems. Services publish the "rules" applications must follow to make use of the service(API)

# Application Program Interface: The API itself is largely abstract in that it specifies an interface and controls the behavior of the objects specified in that interface. The software that provides the functionality described by an API is said to be an "implementation" of the API. An API is typically defined in terms of the programming languiafge used to be build an application.
# http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI

# API Secrurity and Rate Limiting: The compute resurces to run this API are not free, the data provided by these APIs is usally valuable. The data providers might limit the number of request per day, demand an API key, or even charge for usage. They might chnage the rules as things progress.eg Twitter API, Google geolocation API

# PYTHON OBJECTS: More on Data Structures.
# An object is a bit of self-contained code and data. Akey aspect of the Object approach is to brek the problem into smaller understandable parts(divide and conquer). Objects have boundaries that allow us to ignore un-needed detail. We have been using objects all along: String Objects, Integer Objects, Dictionary Objects, List Objects....

# Class: defines the abstract characteristics of a thing (object), including the things characteristics (its attributes, fields or properties) and the things behaviors (the things it can do, or methods operations or features). One might say that a class is a blueprint or factory that describes the nature of something.

# class PartyAnimal:
#      x = 0

#      def party(self):
#       self.x = self.x + 1
#       print("So far", self.x)

# an = PartyAnimal()

# an.party()
# an.party()
# an.party()

# dir()is a function used to find the capabilities of an Objects.
y = "Hello there"
dir(y)  # Shows the capabilities of the String Object: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Object Lifecycle: Objects are created, used and discarded. We have special blocks of code (methods) that get called, -at the moment of creation(constructor) - at the moment of destruction(destructor). Constructors are used alot. Destructors are seldom used.

# Constructor: The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created.

# class PartyAnimal:
#      x = 0
      
#      def __init__(self):
#       print('I am constructed')

#      def party(self):
#       self.x = self.x + 1
#       print("So far", self.x)
     
#      def __del__(self):
#       print('I am destructed', self.x)

# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains', an)

# In object oriented programming, a constructor in a class is a special block of statements called when an object is created.

# In the example below, we have two independent instances of the class PartyAnimal. (S and J)
class PartyAnimal:
     x = 0
     name = ""
     def __init__(self,z):
      self.name = z
      print(self.name, 'constructed')

     def party(self):
      self.x = self.x + 1
      print(self.name, 'party count', self.x)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
