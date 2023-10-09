# Open the file for reading
with open('80s-music.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Process each line here
        print(line.strip())  # For example, print the line after stripping whitespace
