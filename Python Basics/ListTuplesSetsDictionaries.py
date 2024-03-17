## Declaraions

# List
variable_list = ["Computer", "Printer", "TV", "Camera"]
variable_list[0] = "PC"

# Tuple
variable_tuple = ("Computer", "Printer", "TV")

# Set
variable_set = (["computer", "printer", "TV"])

# Dictionary
variable_dictionary = {
    1: "Number",
    "day": "Wednesday"
}

### Adding and removing values

## List
list = []
list.append("Val")
list.pop()

## Tuple
tuple = tuple(list) #Tuples are inmutable

## Set
set = set()
# Add
set.add(1)
# Remove
set.remove(1)

## Dictionaries
d = {}
# Add
d[0] = "Zero"
# Remove
del d[0]
