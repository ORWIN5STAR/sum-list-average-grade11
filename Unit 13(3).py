# Ask user for really big number
bigNumber = input("Enter a really big number: ")

sum = 0

# Use loop to find sum of the number 
for i in bigNumber:
    sum += int(i)

# Print out sum of the number
print(sum)