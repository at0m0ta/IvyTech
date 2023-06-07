#Using Super example


class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + " " + self.last + ", " + str(self.age)

class Employee(Person):
    def __init__(self, first, last, age, salary):
        super().__init__(first, last, age)
        self.salary = salary

    def __str__(self):
        return super().__str__() + ", " + str(self.salary)
    
def main():
    x = Person("Ashwin", "Pajankar", 31)
    print(x)
    y = Employee("James", "Bland", 45, 1000)
    print(y)
    
if __name__ == "__main__":
    main()
