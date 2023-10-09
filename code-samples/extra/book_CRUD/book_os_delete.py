# This program allows the user to delete
# a record in the book.txt file.

import os  # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the book to delete.
    search = input('Which book do you want to delete? ')
    
    # Open the original book.txt file and the temporary file.
    with open('book.txt', 'r') as book_file, open('temp.txt', 'w') as temp_file:
        # Read the first record's title field.
        title = book_file.readline()

        # Read the rest of the file.
        while title != '':
            # Read the quantity field.
            qty = float(book_file.readline())

            # Strip the \n from the title.
            title = title.rstrip('\n')

            # If this is not the record to delete, then
            # write it to the temporary file.
            if title != search:
                # Write the record to the temp file.
                temp_file.write(f'{title}\n')
                temp_file.write(f'{qty}\n')
            else:
                # Set the found flag to True.
                found = True

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