# Assigment 02

We began assignment_02 in class from [looking at this slide](https://docs.google.com/presentation/d/1fredmqsDRSivpXaNQKabISEIoeFbkfhuc-F-QrBV1tM/edit?pli=1#slide=id.g27d7880ce6e_0_83)

Your goal was to take this code:

```
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    
```

And change it to this:

```
items = ['item1', 'item2', 'item3', 'item4']

for item in items:
    print(item.upper())

```
Except you need to change  any occurrence of ```item```, ```items``` and ```item1-4``` to something meaningful to you.

This may seem like a simple exercise if you just copy, paste, and change.

But try to come up with five things in a list and set the method and for/in loop through by memory. You might find that 
to a bit more challenging. This is a very compact bit of knowledge, so practice it over and over so you can do it without referencing the sample. I won't require this for everything, but this it good short bit of code to get into your muscle memory.

Also, as part of assignment 02 I would like for you to finish the code that we started here:

```
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
I mentioned that you did not always need to have a final ```else``` in a program. However, in this
case, you do. Try to enter age 40 and see what you get....nothing. You need a "catch-all" ```else``` in this example. Look at the code samples for help.

Also, I would like for you to adjust the code so that the senior discount is a lower price
for the Centenarian. Don't do the calculation in the print function. just put ```{senior_price}``` and {centenarian_price} in the print function. Under price = 10 variable, change the ```senior_discount = .8``` variable to ```senior_price = price * .8``` and then do the same with ```centenarian_price``` but make the discount deeper (better price.)

When done, just zip up your ```in_class``` folder and name it ```lastname_firstname_assignment_02``` and upload it to Canvas.
