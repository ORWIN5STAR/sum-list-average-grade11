import random

# Random 75 numbers between 15-50
random_numbers = [random.randint(15, 50) for i in range(75)]

# Sort the numbers
newList = sorted(random_numbers)

# Print the list
print(newList)

# Ask user for the target number
target = int(input("Enter target number: "))

# Count the target number
x = newList.count(target)

# Display how many of the target values are in the list.
print(x)