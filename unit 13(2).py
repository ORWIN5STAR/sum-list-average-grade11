# Ask user for a sentence
sentence = input("Enter a sentence: ")

# Make an empty list
list = []

# Use loop to count all letters
for i in range(len(sentence)):
    # Store all letters in list
    list.append(i)

# Print out the list
print(list)