class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"

employee1 = Employee("Іван", "Менеджер", 5000)
print(employee1.get_salary_info()) 
