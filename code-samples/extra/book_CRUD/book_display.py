# This program displays the records in the book.txt file.

def main():
    # Open the book.txt file.
    with open('book.txt', 'r') as book_file:
        # Read the first record's title field.
        title = book_file.readline()

        # Read the rest of the file.
        while title != '':
            # Read the quantity field.
            qty = float(book_file.readline())

            # Strip the \n from the title.
            title = title.rstrip('\n')

            # Display the record.
            print(f'Title: {title}')
            print(f'Quantity: {qty}')

            # Read the next title.
            title = book_file.readline()

# Call the main function.
if __name__ == '__main__':
    main()