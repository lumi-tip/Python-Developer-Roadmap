from queue import LifoQueue

my_stack = LifoQueue()

my_stack.put("a")
my_stack.put("B")
my_stack.put(3)

try:
    while True:
        print(my_stack.get_nowait())
except:
    print("Empty Stack")