import random # --> Eso lo importamos para que la lista sea randomizada siempre
import heapq

"""
heap provides functions to work with binary heaps that are basically binary trees whose difference is that they can be of the type minimum binary heap
or maximum binary heap. The former are characterized because the children are larger than the root node and in the latter the children are smaller than the root node.

"""

random_list = [34,234,5,6,1,233,445,653,344,123,56]

print("-----THIS IS THE LIST YOU ARE WORKING WITH------")
print(random_list)
print(' ')

## Transformar una lista en un heap 
heapq.heapify(random_list)
print("-----THIS YOUR HEAP------")
print(random_list)

## Add an item to your heap
heapq.heappush(random_list, 9)
print("-----ADDING ELEMENT 9------")
print(random_list)

## delete the lowest item in the heap
heapq.heappop(random_list)
print("-----REMOVING LOWEST ELEMENT------")
print(random_list)

## Add an element and remove de lowest, it returns the popped element
lowest_pushpop = heapq.heappushpop(random_list, 2)
print("-----ADDING ELEMENT 2 AND REMOVING LOWEST ELEMENT------")
print(f'lowest element was --> {lowest_pushpop}')
print(f'Your list now --> {random_list}')

## Remove the lowest and add an element, returns the popped element
lowest_replace = heapq.heapreplace(random_list, 2)
print("-----REMOVING LOWEST ELEMENT AND ADDING ELEMENT 2------")
print(f'lowest element was --> {lowest_replace}')
print(f'Your list now --> {random_list}')

## get the n largest items
print("-----LARGEST N ITEMS------")
largest_heap = heapq.nlargest(4, random_list)
print(largest_heap)

## get the n smalles items
print("-----SMALLEST N ITEMS------")
smallest_heap = heapq.nsmallest(4, random_list)
print(smallest_heap)