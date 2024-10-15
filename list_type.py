# Create a list with 4 numbers
my_list = [21, 53, 85, 46]

# Print the first item in the list
print(my_list[0])

# Print the last item in the list
print(my_list[-1])

# Print the first two items
print(my_list[:2])

# Add a new item at the end of the list such that it’s the addition of the first and last item in the list:
my_list.append(my_list[0] + my_list[-1])
print(my_list[-1])