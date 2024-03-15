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

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("B")
    except C:
        print("C")
    except B:
        print("D")