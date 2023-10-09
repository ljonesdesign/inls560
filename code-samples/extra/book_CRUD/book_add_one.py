# This program adds title and quantity records to
# the book.txt file.

# function is added 

def main():
   
    # Open the book.txt file in append mode.
    with open('book.txt', 'a') as book_file:
      
        print('Enter the following book data:')
        title = input('Title: ')
        qty = int(input('Quantity in Stock: '))

        # Append the data to the file.
        book_file.write(f'{title}\n')
        book_file.write(f'{qty}\n')

    print('Data appended to book.txt.')

# Call the main function.
if __name__ == '__main__':
    main()