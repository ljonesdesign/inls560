# Assignment 02

We began assignment_02 in class from [looking at this slide](https://docs.google.com/presentation/d/1fredmqsDRSivpXaNQKabISEIoeFbkfhuc-F-QrBV1tM/edit?pli=1#slide=id.g27d7880ce6e_0_83).

Your goal was to take this code:

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    
```

And change it to this:

```python
items = ['item1', 'item2', 'item3', 'item4']

for item in items:
    print(item.upper())

```
Except you needed to change  any occurrence of ```item```, ```items``` and ```item1-4``` to something meaningful to you.

This may seem like a simple exercise if you just copy, paste, and change.

But try to come up with four things in a list and code it from memory. Where do the commas go? Did you remember the proper position of the quotes? Come back later and try it again. What was the keyword for a loop? Was it a ```for``` loop or a ```while``` loop? Did you forget the ```in``` keyword? How did we get that ```upper()``` method in there? 

There is actually a lot going on in this little block of code. And you will use this a lot as you continue to code so practice it over and over so you can do it without referencing the sample. I won't require this for everything, but this it good short bit of code to get into your muscle memory as it covers ```lists```, the ```for``` loop and a method, ```upper()```, in one go. 

The goal for this week activity is *quality* over *quantity*. Or *depth* as opposed to *breadth*. 

The the second part part of assignment 02, I would like for you to finish, and edit, the code that we started. Try to enter age 40 and see what you get....nothing.
I mentioned that you did not always need to have a final ```else``` in a program. However, in this case, you do.  You need a "catch-all" ```else``` in this example. Look at the code samples for help.

```python
# Amusement Park Admission

price = 10
senior_discount = .8
age = int(input("What is your age: "))

if age > 100:
    print(f'Welcome Centenarian. Your admission is {price * senior_discount}')
elif age > 60:
    print(f'you get a discount. Your admission is {price * senior_discount}')
elif age < 5:
    print (f'you get free admission! No Charge!')

```

And finally, adjust the code so that the senior discount is a lower price for the Centenarian. Don't do the calculation in the print function as we did in class. Instead put in ```{senior_price}``` and ```{centenarian_price}``` in each print function. Below the ```price = 10``` variable, change the ```senior_discount = .8``` variable to ```senior_price = price * .8``` and then do the same with ```centenarian_price``` but make the discount deeper (better price.)

When done, just zip up your ```in_class``` folder and name it ```lastname_firstname_assignment_02``` and upload it to Canvas.
