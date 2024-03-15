## Saving a Value
n = 200

## Saving multiple values

a = b = c = 200
## Or 

a,b = 10,20

## Assigment Type
# Int Assigment
integer = 43

# Float Assigment

float = 14.4

# String assigment

string = "luis"

# Boolean Assigment

boolean = True

# None assigment

none_type = None

# Complex Assigment

cpx = (2+3j) #To study

# Local Assigment
def localAssigment():
    local_var = "I'm a local variable"
    print(local_var)

# Global Assigment
global_var = "I'm a globar variable"

def globalAssigment():
    print(global_var)

# Global assigment inside a function
    
def globalAssimentInFunction():
    global global_variable_function
    global_variable_function = "Im a global inside a local environment"


## Function Exec

localAssigment()
# print(local_variable) ------> this throw an error
globalAssigment()
print(global_variable_function) #------> This will NOT throw error

## Typing

print(type(a))
print(type(2))
print(type("String"))
print(type(none_type))
print(type(boolean))

## Base Interpreter

# Bynary base
print(0b10)

## Octal base
print(0o10)

## Hexadecimal base
print(0x10)