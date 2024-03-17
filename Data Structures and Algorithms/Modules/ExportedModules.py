## Functions and Class exports

class ExportedClass:
    def __init__(self,name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'I am {self.name}, I have {self.age} years old'
    
def exportedFunction():
    print('I am the exported function')