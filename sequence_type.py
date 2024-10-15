# 1) Create a list of 5 items having combination of  (integer, float, strings) as items.
items = [ 1, 2.62, "str", 726 + 1, "p"]

# 2) Print the length of your list
print(len(items))

# 3) Add an extra item to the end of the list
items.append("added")

# 4) Add any item to the beginning of the list
items.insert(0, 12)

# 5) Remove the last item in the list
items.pop()

# 6) Find the length of list
print(len(items))

# 7) Print the value of the first item of your list
print(items[0])

# 8) Change the second item in your list by any value.
items[1] = 262.262

# 9) Verify the data type of your sequence
print(type(items))

# 10) Convert your list to tuple
items_tuple = tuple(items)

# 11) Verify the data type of your tuple
print(type(items_tuple))

# 12) Access the first value in your tuple
print(items_tuple[0])

# 13) Find the length of the tuple
print(len(items_tuple))

# 14) Try to change the value of the first item in your tuple
# items_tuple[0] = "unmodifiable"
# Will throw a TypeError as you can't assign to a tuple as they are unmodifiable

# 15) Create another tuple of any size.
new_tuple = (2, 6, 2, "Tuple")

# 16) Join the two tuples into a single tuple
joined_tuple = items_tuple + new_tuple

# 17) Print the joined tuple
print(joined_tuple)

# 18) Convert the joined tuple in to a list
joined_list = list(joined_tuple)

# 19) Verify the data type of the list
print(type(joined_list))

# 20) Convert your list to set
joined_set = set(joined_list)

# 21) Find the length of the set
print(len(joined_set))

# 22) Add an item to your set.
joined_set.add(262)

# 23) Print your set
print(joined_set)

# 24) Add another item to your set (which already exists)
joined_set.add(262)

# 25) Print your set. Notice that the duplications are not allowed.
print(joined_set)

# 26) Create another set
new_set = {262, "Tuple", "p", 727, "not common"}

# 27) Find the common items between the two sets
intersection = joined_set & new_set
print(intersection)

# The & operator performs the intersection between two sets. Only leaving the items that are common in both the sets