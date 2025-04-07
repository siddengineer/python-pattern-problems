# Full Diamond Pattern Generator
# Example for size = 4:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# Set the size of the upper half of the diamond
size = 4

# Print the upper half of the diamond
# Including the middle row
for i in range(size):
    # Print spaces to center the stars
    # As i increases, the number of spaces decreases
    spaces = size - i - 1
    stars = 2 * i + 1  # Stars form an odd number: 1, 3, 5, ...

    # Display the row
    print(" " * spaces + "*" * stars)

# Print the lower half of the diamond
# Starts from size - 2 to avoid repeating the middle row
for i in range(size - 2, -1, -1):
    spaces = size - i - 1  # Spaces increase again
    stars = 2 * i + 1      # Stars decrease symmetrically

    # Display the row
    print(" " * spaces + "*" * stars)
