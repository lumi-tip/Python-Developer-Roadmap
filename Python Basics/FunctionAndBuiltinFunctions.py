## Basic Function Example
def exampleFuntion():
    print("This is a simple funtion")
exampleFuntion() # --> result This is a simple funtion

## Basic Lambda Function
lambda_funtion = lambda name: print(name)
lambda_funtion("Lambda function")

## With return satement
def addTwo(a):
    return a + 2
print(addTwo(10)) # --> result 12

## Function with unknown number of parameters
def functionNParams(*params):
    print(f'This function has {len(params)} elements and the first one is {params[0]}')
functionNParams("Maria", "Jose", "Luis")

## Function with keyboard arguments
def namesFunction(param_one, param_two, param_three):
    print(f'First Param: {param_one}, Second Param: {param_two}, Third Param: {param_three}')
namesFunction(param_three="Juan", param_one= 1, param_two=True)

## Funtion With Arbitrary Keyword Arguments
def arbitraryArguments(**keys):
    print(keys)
arbitraryArguments(name = "Arbitrary", last_name="Arguments")

## Function with default value
def defaultValFunction(name = "Default Arg Function"):
    print(name)
defaultValFunction()

## Function that only expects one argument:
def oneArgumentFunction(arg,/):
    print(arg)
oneArgumentFunction("One Arg Function")
# oneArgumentFunction("Luis","vero") --> This will thorw an error

## Function with only keywords:
def onlyKeywordsFunction(a, b, /, *, c, d):
    print(a + b + c + d)
onlyKeywordsFunction(5, 6, c = 1, d = 3)
# onlyKeywordsFunction(5, 6, 1, 3) --> this throws an error