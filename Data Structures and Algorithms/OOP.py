## Oriented Object Programing Example
class Human:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f'{self.name} has {self.age} years and his gender is {self.gender}'
    
class Employee(Human):

    salariesArr = []

    def __init__(self, name, age, gender, salary) -> None:
        super().__init__(name, age, gender)
        self.department = None
        self.salary = salary
        self.salariesArr.append(salary)
    
    def compareSalary(self, person):
        if isinstance(person, Employee):
            if self.salary < person.salary:
                return f'{person.name} earns {person.salary - self.salary} more than {self.name}' 
            elif self.salary > person.salary:
                return f'{self.name} earns {self.salary - person.salary} more than {person.name}'
            else: return f'Both Employees have the same salary'
        else: 
            raise(f'{self.name} is not an Employee')
    
    def __add__(self, person):
        if isinstance(person, Employee):
            return person.salary + self.salary
        else:
            raise (f'{person} is not an employee')
        
    @classmethod
    def getEmployeesCost(cls):
        total_cost = 0
        for salary in cls.salariesArr:
            total_cost += salary
        return f'Labour Cost: {total_cost}'
    
    @property
    def Department(self):
        return self.department
    
    @Department.setter
    def Department(self, new_depart):
        self.department = new_depart

    @Department.deleter
    def Department(self):
        if self.department is not None:
            print(f'{self.department} was deleted from {self.name}')
            self.department = None
        else:
            raise AttributeError(f'{self.name} does not belong to any department')
    
## Object Testing
        
if __name__ == "__main__":
    test_person = Human("Jose", 15, "Male")
    test_employee_one = Employee("Luis", 22, "Male", 300)
    test_employee_two = Employee("Temis", 23, "Male", 200)
    test_employee_three = Employee("Juan", 42, "Male", 200)

    print(test_person)
    print(Employee.compareSalary(test_employee_two, test_employee_one))
    print(Employee.compareSalary(test_employee_two, test_employee_three))

    # print(test_person + test_employee_two) --> This throws an error as test_person is not an employee
    print(test_employee_two + test_employee_one) # --> this sums salaries

    print(Employee.getEmployeesCost())

    print(test_employee_three.department)
    test_employee_three.department = "Sales Man"
    print(test_employee_three.department)
    test_employee_three.department = "CEO"
    print(test_employee_three.department)

    del test_employee_three.department
    try:
        print(test_employee_three.department)
    except AttributeError as e:
        print(e)

