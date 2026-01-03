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

# Paseltongue is the langiage of the serpants and those who can converse with them. It is a hissing, sibilant langiuage that is difficult for most to learn. An individual who can speak paseltongue is known as a Parselmouth. It is a very uncommon skill, and may be hereditary. Nearly all known Parselmpouths are descended from Salazar Sytherin. 

# Python Reserved words: False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# Variables, Expressions and Statements
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

# Functions: A function is a named block of code that performs a specific task. Functions are used to organize code and make it more reusable. In python, a function is a reusable code that takes argument(s) as input, do some computation, and returns a result. We call/invoke the function by using the function name, parentheses, and arguments in an expression. Functions are defined using the def keyword. 
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

#Loops and Iteration: Loops are used to repeat a block of code multiple times. In python, loops are implemented using the for and while statements. eg: 
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

# Lists: A list is a collection of items that are ordered and changeable. Lists are defined using square brackets [] and items are separated by commas. eg:
fruits = ['apple', 'banana', 'orange']
print(fruits)
# Accessing list items

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

# Reading and Writing Files: You can read from and write to files using string manipulation techniques. This is useful for processing text data stored in files.
# eg:
fhand = open('mbox-short.txt')
for line in fhand:
     line = line.rstrip()
     if line.startswith('From:'):
          print(line)

# File Processing: A text file is a sequence of lines of text. Each line is terminated with a special character called a newline character. When you read a file, you get the newline character as part of the line. To remove the newline character from the end of the line, you can use the rstrip() method. eg:

