# This program adds title and quantity records to
# the book.txt file.

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the book.txt file in append mode.
    with open('book.txt', 'a') as book_file:
        # Add records to the file.
        while another == 'y' or another == 'Y':
            # Get the book record data.
            print('Enter the following book data:')
            title = input('Title: ')
            qty = int(input('Quantity in Stock: '))

            # Append the data to the file.
            book_file.write(f'{title}\n')
            book_file.write(f'{qty}\n')

            # Determine whether the user wants to add
            # another record to the file.
            print('Do you want to add another book title?')
            another = input('Y = yes, anything else = no: ')

    print('Data appended to book.txt.')

# Call the main function.
if __name__ == '__main__':
    main()