# Assignment 01

Below is the exact output goal of this assignment including the labels and the spacing. Before turning in your project choose different numbers from the defaults of ```a = 10``` and ```b = 3```. (```c``` should remain as ```2```, however.)

```python
a = 10 # a can be any digit > 1 and < 10
b = 3  # b can be any other digit > 2 and < 10 
c = 2
```

```
Addition:        10 + 3 = 13
Subtraction:     10 - 3 = 7
Multiplication:  10 * 3 = 30
Division:        10 ÷ 3 = 3.3333333333333335
Floor Division:  10 ÷ 3 = 3
Modulo:          10 % 3 = 1
Exponent:        10 + 3² = 19

Division 
(dollars):       10 ÷ 3 = $3.33
```

This is not difficult math, but the coding of the strings, tabs, and spacing can be a bit of a challenge. You are not allowed to use any actual numbers in the code. You must reference variables only.

If you have time before class, see how much of this you can get done on your own. Contact me via email if something is not clear.

To get started:

Create a folder on your computer and name it:

```
lastname_firstname_assignment_01
``` 

In that folder, create a python file named:

```
assignment_01.py
```

Copy and paste the code below into the file you created. 

Don't try to select it. To easily copy the code, hover over the top right corner of the code box and you will see a copy-code icon appear. Click that, and you will be able to then paste that code into your file.

![copy code](/img/copy-code.png)

Follow the directions in the comments. Edit the comments so that they no longer read as instructions, but read as documentation. When you are done, zip up the folder and upload it to the assignments in Canvas by the due date.

*01_assignment.py*

```python
# Create three int variables. Choose any number that meets the requirement

# You do not need to attempt to create the number from code manipulation; 
# just choose a simple integer like 10 and 3 in the  above sample.

# a can be any digit > 1 and < 11 
# b can be any other digit > 2 and < 10 
# c must be 2

''' Multi-line comment example
This program will throw an error if the variables are not set first. 
After you set these variables the complete and incomplete 
print statements will run to give you a head start.
'''

# Create a list of all the math operations. Addition has been done for you:

# Print Addition and a tab then show a '+' b '=' a + b. 
# Notice how the operators must be in quotes to be treated as plain text
# and not operators.
print('Addition:\t', a, '+', b, '=', a + b)

# Do the same for the following:
# Hint, copy and paste the sample above, but be very careful 
# to make all needed edits!

# Subtraction
print()

# Multiplication
print()

# Division (do an internet search on the division sign for 
# string and copy paste it.)
print()

# Floor Division (use the same copied division sign here for string output)
print()

# Display remainder after division (Modulo)
# May need extra \t because Modulo is the shortest label.
print()

# Display Exponent a + b squared. Make it fit the output pattern. 
# Use variable c in the code, not an actual number 2.

# u'\xb2' is the python escape for 2 superscript. Use this to 
# output the 2 superscript.

# Set it as a string literal variable.

# Call the string literal variable in the print function.

# Use a valid variable name don't use the example var.

# Below is a working sample to get your started:

# var = (see the escape above; this one is tricky!) 

# Don't forget to use labels for consistent output
var = 'sample_string'
print(f'yourcode yourcode {var} yourcode')

'''
Division with currency output with f string: {a/b:???} = $ ?.??
Don't forget to use labels for consistent output. Add a new line at
the start of this string to separate it from the previous strings.
Sample:

Division 
(dollars):       10 ÷ 3 = $3.33
'''

print(f'{a/b:}')
```