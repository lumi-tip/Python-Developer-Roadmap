## Implicit conversion

integer = 1
floating = 1.5
implicit_coversion = integer + floating
print(type(implicit_coversion)) #--> Prints a float

## Explicit conversion

num_string = '12'
explicit_convertion = int(num_string)
print(type(explicit_convertion)) #--> Prints a Intager

## Exceptions

while True:
    try:
        x = int(input("Escribe un numero entero"))
        print(x)
        break
    except ValueError:
        print("It MUST be an integer")

# Multiple Exceptions
        
class B(Exception):
    pass

class C(Exception):
    pass

class D(Exception):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except B:
        print("C")
    except C:
        print("D")

# Expections With Parameters

try:
    raise Exception("spam", "eggs")
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

# Exception in function
    
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Custom Message') from exc

# Exceptions Finally Clause

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')