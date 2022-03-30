#find the total number of characters in travel_plans.txt

num = 0

with open("travel_plans.txt") as file:
    data = file.read()
    num = len(data)
    
# print(num)

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

first_chars = ""

with open("travel_plans.txt") as file:
    data = file.read()
    first_chars = data[:33]

# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.

num = 0

with open("travel_plans.txt") as file:
    data = file.read()
    num = len(data)