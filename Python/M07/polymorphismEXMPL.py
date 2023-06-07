#Polymorphism example


class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + " " + self.last + ", " + str(self.age)

class Employee(Person):
    def __init__(self, first, last, age, salary):
        self.first = first
        self.last = last
        self.age = age
        self.salary = salary
    def __str__(self):
        return self.first + " " + self.last + ", " + ", " + str(self.age) + ", " + str(self.salary)
def main():
    x = Person("Ashwin", "Pajankar", 31)

    y = Employee("James", "Bland", 45, 1000)
    
    print(x," | ", y)
    
if __name__ == "__main__":
    main()
