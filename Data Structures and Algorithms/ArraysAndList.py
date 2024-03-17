import array as arr
'''
arrays and lists are not the same in python, 
arrays contains ont type of value but lists contain different
types of values

'''
## Array creation
create_arr = arr.array("i")
print(create_arr)

## List Creation
list_test = []
list_test = list()
print(list_test)

## Defining an arr in python
test_arr = arr.array("i", [1,2,3,4,5,444])
print(test_arr)

## Length
print(len(test_arr))

## Accessing to a data
print(test_arr[0])

## Search through an array
print(test_arr.index(444)) # Expect to return 5 if there is more than one it will return the first that it founds

## add value at the end a new value
test_arr.append(555)
print(test_arr)

## Extend an array
test_arr.extend([1,2,3])
print(test_arr)

## add a value somewhere
test_arr.insert(0,99) # --> First is the index sendond is the value
print(test_arr)

## Remove a value (Works same as index)
test_arr.remove(99)
print(test_arr)

## Delete last value
test_arr.pop()
print(test_arr)

### EXERCISES
print("-------------------EXERCISES---------------------")

# Create an arr of integuers with this numbers 1,2,3,4
learn_arr = arr.array("i",[1,2,3,4])
print(learn_arr)

# Access to the last element of the arr
print(learn_arr[len(learn_arr) - 1])

# Search the index of number 2 in the array:
print(learn_arr.index(2))

# Add the value 333 at the end of the arr:
learn_arr.append(333)
print(learn_arr)

# Add at the end of the array this arr [4,5,6]
learn_arr.extend([4,5,6])
print(learn_arr)

# Add the value 99 at the begining of the arr:
learn_arr.insert(0,99)
print(learn_arr)

# Remove the value 4 from the arr:
learn_arr.remove(4)
print(learn_arr)

# Remove the last item fro the arr
learn_arr.pop()
print(learn_arr)

