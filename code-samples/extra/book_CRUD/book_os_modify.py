# This program allows the user to modify the quantity
# in a record in the book.txt file.

import os  # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = input('Enter a title to search for: ')
    new_qty = int(input('Enter the new quantity: '))
    
    # Open the original book.txt file and a temporary file.
    with open('book.txt', 'r') as book_file, open('temp.txt', 'w') as temp_file:
        # Read the first record's title field.
        title = book_file.readline()

        # Read the rest of the file.
        while title != '':
            # Read the quantity field.
            qty = float(book_file.readline())

            # Strip the \n from the title.
            title = title.rstrip('\n')

            # Write either this record to the temporary file,
            # or the new record if this is the one that is
            # to be modified.
            if title == search:
                # Write the modified record to the temp file.
                temp_file.write(f'{title}\n')
                temp_file.write(f'{new_qty}\n')
                
                # Set the found flag to True.
                found = True
            else:
                # Write the original record to the temp file.
                temp_file.write(f'{title}\n')
                temp_file.write(f'{qty}\n')

            # Read the next title.
            title = book_file.readline()

    # Delete the original book.txt file.
    os.remove('book.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'book.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# Call the main function.
if __name__ == '__main__':
    main()