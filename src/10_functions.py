# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x % 2 == 0:
        return 'true'
    else:
        return 'false'


print(is_even(800))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def input_even(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")


input_even(num)
