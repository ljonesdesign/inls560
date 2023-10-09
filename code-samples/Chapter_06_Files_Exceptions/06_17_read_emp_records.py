# This program displays the records that are
# in the employees.txt file.

def main():
    # Open the employees.txt file.
    with open('employees.txt', 'r') as emp_file:
        # Read the first line from the file, which is
        # the name field of the first record.
        name = emp_file.readline()

        # If a field was read, continue processing.
        while name != '':
            # Read the ID number field.
            id_num = emp_file.readline()

            # Read the department field.
            dept = emp_file.readline()

            # Strip the newlines from the fields.
            name = name.rstrip('\n')
            id_num = id_num.rstrip('\n')
            dept = dept.rstrip('\n')

            # Display the record.
            print(f'Name: {name}')
            print(f'ID: {id_num}')
            print(f'Dept: {dept}')
            print()

            # Read the name field of the next record.
            name = emp_file.readline()

# Call the main function.
if __name__ == '__main__':
    main()