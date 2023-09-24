# Assignment 04

## Part A
**concepts:**  *priming a `while` loop, executing a `while` loop, printing a menu, quitting a while loop, using `sep="\n"` (to print new lines), get user `input` to continue loop, use `if` and `elif` to control chosen output*

In **part A** we will print a menu that will continue to (while) loop again and again. The goal is for it to look like this example that was shown in class. Be sure to change the menu and your code to be something original. That will make it your own and fire up extra neuron connections in your brain to make this program pattern more memorable.

```
MENU:
a: cut and fold brochures
b: deliver print jobs
q: quit
Enter a letter for more info around the shop:
```
The menu is short with only three options: a, b, and q for quit. Just having two choices makes it seem unnecessary to loop; however, you could create a menu with 10 to 20 items, like in a FAQ. In that case it makes sense for it to loop again and again to allow multiple interactions. The user could continue to choose various FAQs and read each one until they decided to quit by pressing `q`.

After the print menu runs, the user will be prompted to enter a letter an a, b, or q. When the user enters a letter, an `if` and an `elif` statement will be necessary to print out the appropriate response to the letter choice. If the user types in a q, the program will exit without running the `if` or `elif` statement.

After the `if` or `elif` runs, the program returns back to the beginning then encounters the `while` statement and runs the program again. It the user was not given the option to quit, it would never stop looping. It would be necessary to "kill" the python session by closing down the application or terminal.

### How to code this:

>As much as possible type all of this out yourself as you will benefit from going through it line by line.

1. Create a `lastname_first-initial_assignment_4` folder. Inside of that folder, create a file named ```while_menu.py```.

2. On the first line of `while_menu.py` file, prime the `while` loop by typing:

```python 
menu_option = ''
```
This creates a variable with no data. Sort of like an empty box with a `menu_option` label. This gives the user a place to store his letter choice. It starts out empty so that the loop will run and then the user can control the loop.

3. On the next line of the program put in your `while` statement. In this case our while statement goes as follows:

```
while | some_variable  |  comparison operator   |  'string' |  FINAL COLON
-----   -------------     -------------------      --------    -----------
while | menu_option    |  != (is not equal to)  |  'q'      |  :
```
The above spaces and grid are for instructional clarity. You will need to type it like this:

```python
while menu_option != 'q':
```
So if the user enters anything, any key at all, except a `q`, it will just keep looping. It takes an actual `a` or `b` for the `if` or `elif` to print a specific response. After you write the program, try it. You can enter anything. It will just loop and loop. It will only pay attention to you if you enter a, b, or q.

4. On the next line program a print function `print()` to present the menu to the user.

Use the regular method (non f-string) of separating the menu items with commas. If you forget to add the final `sep="\n"` the text will print all on one line as shown below:

Code:
```python
print('MENU:','a: cut and fold brochures', 'b: deliver print jobs', 'q: quit')
 ```
Output:
 ```
 MENU: a: cut and fold brochures b: deliver print jobs q: quit
 ```

 Therefore, add a comma after the quit string and add the the `sep="\n"` to make each choice print out on a new line as is shown at the top of the assignment instructions.

 After the user is sees the menu they also need see a prompt to enter the input. This can't be combined with the menu because the input needs to be assigned to the `menu_option` variable.  It is important to understand that the logic is tied to the `if` and the `elif`. The menu is just directions. The input message is just directions. **What matters is that the variable gets stored and the if and the elif are watching for it.**

 Okay, now we are getting into the logic. This is where you construct your `if` and `elif`:

 ```python
 if menu_option == 'a':
    print('response a')
elif menu_option == 'b':
    print('response b')
  ``` 

This will complete this first part of assignment 4.

## Part B

**concepts:**  *practice with f- strings, nested `while` loop*

For part B you will simply duplicate your `while_menu.py` file and name the duplicated file `while_menu_nested.py` it should be in the same `lastname_first-initial_assignment_4` folder

In this version do not use the `sep='\n'` for new lines. Use a f-string like this:

```python
print('''
Shop information FAQS:
a: cut and fold brochures
b: deliver print jobs
q: exit 
''')
```
Then under your elif add another `variable = input('string (y or n): ')` and a nested if else. The if will accept the `y` and the else will accept the `n`. Remember to use some other example other than what we did in class.

```python

 if menu_option == 'a':
        print('The cutter and folder can be dangerous. Get training before using!')
    elif menu_option == 'b':
        van_driver = input('Are you comfortable driving a class B van? enter (y or n): ')
        if van_driver == 'y':
            print("Awesome! It would be great to have you help deliver on occasion!")
        else:
            print("We won't ask you to drive!")
```

When finished, zip up your folder and submit it in Canvas for Assignment 04.
