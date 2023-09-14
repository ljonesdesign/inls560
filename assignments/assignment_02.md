# Assigment 02

We began assignment to in class from [looking at this slide](https://docs.google.com/presentation/d/1fredmqsDRSivpXaNQKabISEIoeFbkfhuc-F-QrBV1tM/edit?pli=1#slide=id.g27d7880ce6e_0_83)

Your goal was to take this code;

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
Except you need to change thing and things to something meaningful to you.

This may seem like a simple excercise. And it is if you just copy and paste and change.

But try to come up with five things and loop through by memory. You might find that 
to a bit more challenging.

Also, as part of assignment 02 I would like for you to finish the code that we started here:

```
# Amusement Park Admission

price = 10
senior_discount = .8

age = int(input("What is your age: "))

if age > 100:
    print(f'Welcome Centarian. Your admission is {price * senior_discount}')
elif age > 60:
    print(f'you get a discount. Your admission is {price * senior_discount}')
elif age < 5:
    print (f'you get free admission! No Charge!')

```
I mentioned that you did not always need to have a final else in a program. However, in this
case, you do. Try to enter age 40 and see what you get....

Also, I would like for you to adjust the code so that the senior discount is a lower price
for the Centarian. Don't do the calculation in the print function. just put `{senior_price} and {centurian_price}
in the print function. Under price = 10 set the varible as senior_price = price * .8 and then do the same with centurian_price but make the discount deeper (better price.)

You can just zipup your in_class folder and name it lastname_firstname_assignment_02 and upload it to Canvas.