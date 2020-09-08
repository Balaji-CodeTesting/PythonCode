# Print HELLO From this given string (Slicing)

# String Declaration
a, b = "AHCECLWLXO", "ahceclwlxo"
c = "0123456789"
print(a[1::2])
print((b[1::2]).upper())
print(c[1::2])

# List[]: we can update in existing data - Mutable
value = [1, 2, 3, "Hello"]
value[3] = "6"
print(value)


# Tuple(): we can't update in existing data - immutable

val = (1, 2, "Hello", 6.2)
# val[2] = "Morning":won't be able to assign new value
print(val)

# Dictionary : key & value pair Combination

dicty = {1: "Hey", 2: "Good", 3: "Morning", "C": "Team"}
print(dicty)
print(dicty[2])
print(dicty["C"])

# Empty Dictionary & adding values

dist = {}
dist["Firstname"] = "Vinodh"
dist["Lastname"] = "Balaji"
dist["Surname"] = "P G"
print(dist)

