# pattern_drawing.py

# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns (printing asterisks)
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after finishing one row
    row += 1  # Increment the row counter
