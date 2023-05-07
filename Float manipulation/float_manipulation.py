import math

num_list = []

i = 0

print("You will be prompted to enter 10 numbers separately!!")
print("They can also be decimals!")
num_input = float(input("Please input a number: "))

# Stores user input into num_list as a list
num_list.append(num_input)

# A while counter for user input
# Continues to loop until 9 entries have been made during the loop
# The total amount of entries will be 10 because there is also the first entry that was outside this loop
# Each time the user inputs a number, it is added to num_list
while i < 9:
    i += 1
    num_input = float(input("Please input another number: "))
    num_list.append(num_input)

# Creates a total for the values in num_list
sum_list = sum(num_list)

print(" ")

print(f'Your list of chosen numbers are: {num_list}')

print(" ")

print(f'The total for all of the numbers is: {sum_list}')

print(" ")

# Prints the index of the highest value in the list
print(f'The index of the maximum value is: {num_list.index(max(num_list))}')

print(" ")

# Prints the index of the lowest value in the list
print(f'The index of the minimum value is: {num_list.index(min(num_list))}')

print(" ")

# Works out the average of the values in the list and rounds to 2.d.p
print(f'The average of these values to 2.d.p is: {round((sum_list / 10), 2)}')

print(" ")

# Sorts the list into ascending order
sorted(num_list)

# The median calculation is as follows: (n+1) / 2 . Here n would be 10. Gives index 5.5
# Index 5.5 will be the average of index 5 and index 6.
# Prints median value for index 5.5
print(f'The median for these values is: {(num_list[5] + num_list[6]) / 2}')
