# Looping through List of 80s Songs

To open the `80s-music.txt` file and loop through its contents, you can use the `open()` function to open the file, and then use a `for` loop to iterate through the lines in the file:

```python
# Open the file for reading
with open('80s-music.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Process each line here
        print(line.strip())  # For example, print the line after stripping whitespace
```
We use the with statement to open the file. This ensures that the file is properly closed when the block of code is exited, even if an exception is raised.

We open the file in `'r'` mode, which stands for read mode. This allows us to read the file's contents.

Inside the `for` loop, we iterate through each line in the file using for line in file.

You can process each line as needed inside the loop. In the example, we simply print each line after stripping any leading or trailing whitespace using the strip() method.

# 