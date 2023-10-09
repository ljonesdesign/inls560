# This program allows the user to search the book.txt
# file for records matching a title.

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    search = input('Enter a title to search for: ')

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

            # Determine whether this record matches
            # the search value.
            if title == search:
                # Display the record.
                print(f'Title: {title}')
                print(f'Quantity: {qty}')
                print()
                # Set the found flag to True.
                found = True

            # Read the next title.
            title = book_file.readline()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print('That book was not found in the file.')

# Call the main function.
if __name__ == '__main__':
    main()