# Define the contains text you want to filter by

contains_to_filter = input("Enter part of an 80s song or Artist: ")

# Open the file for reading
with open('80s-music.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Check if the line starts with the specified prefix
        if line.__contains__(contains_to_filter):
            # Process or print lines that start with the prefix
            print(line.strip())  # For example, print the filtered line after stripping whitespace
        else:
            print("The list does not contain that text.")
