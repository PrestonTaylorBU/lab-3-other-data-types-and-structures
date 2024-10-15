# 1) Create a new dictionary with key-value pairs for a car.
car_details = { "date": 2021, "manufacturer": "Audi", "model": "R8"}

# 2) Print the dictionary
print(car_details)

# 3) Retrieve and print the value associated with a specific key
car_date = car_details["date"]
print(car_date)

# 4) Print the dictionary
print(car_details)

# 5) Modify the value associated with a key.
car_details["date"] -= 1

# 6) Print the dictionary
print(car_details)

# 7) Add a new key-value pair to the dictionary.
car_details["price"] = 22000

# 8) Print the dictionary
print(car_details)

# 9) Delete a key-value pair from the dictionary.
del car_details["price"]

# 10) Print the dictionary
print(car_details)