# This program adds one title quantity record to book.txt file.

# No main function to show that this will work without a function.

# Open the book.txt file in append mode.
with open('book.txt', 'a') as book_file:
      
    print('Enter the following book data:')
    title = input('Title: ')
    qty = int(input('Quantity in Stock: '))

    # Append the data to the file.
    book_file.write(f'{title}\n')
    book_file.write(f'{qty}\n')

print('Data appended to book.txt.')
