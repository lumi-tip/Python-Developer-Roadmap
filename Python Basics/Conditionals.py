## Conditions statements if elif else
def standardConditions():
    if (x > y): print("x is greater than y")
    elif(x < y): print("y is greater than x")
    else: print("x is equal to y")

## Conditions switch statement (with dictionary)
def switchStatement():
    switcher = {
        0: "Case zero",
        1: "Case one",
        2: "Case two",
    }
    return print(switcher.get(cases, "Non Existent Case"))

def rowCondition():
    row_condition = "X and Y has the same value" if x == y else "X and Y have different values"
    print(row_condition)

def matchStatement():
    match cases:
        case 0: print("This is case 0")
        case 1: print("this is case 1")
        case 2: print("this is case 2")
        case other: print("no match found")

# Exec
if(__name__ == "__main__"):
    x = int(input("x: "))
    y = int(input("y: "))
    cases = int(input("switch case: "))

standardConditions()
switchStatement()
rowCondition()
matchStatement()

