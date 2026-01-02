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

#Loops and Iteration: Loops are used to repeat a block of code multiple times. In python, loops are implemented using the for and while statements. eg: 
